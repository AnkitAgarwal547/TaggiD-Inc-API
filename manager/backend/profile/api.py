import json
import logging
from django.http import JsonResponse

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from backend.gamification.serializers import GameProfileSerializer, LeaderBoardSerializer

from ..analytics.profile.utils import send_profile_view_count_notification

from ..gamification.models import GameProfile
from ..gamification.utils import determine_gamification_tier, TaggTierException

from ..common.image_manager import header_pic_url, profile_pic_url
from ..models import ProfileTutorialStage, TaggUser
from ..moments.moment_category.utils import (
    get_moment_categories,
    get_recent_moment_on_profile,
)
from ..social_linking.utils import get_linked_socials
from .utils import (
    allow_to_view_private_content,
    get_profile_info_serialized,
)
from ..common.notification_manager import (
    NotificationType,
    handle_notification_with_images,
)
from django.db.models import F
import pytz
from datetime import datetime, timedelta
from django.utils.timezone import localtime



class ProfileViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def __init__(self, *args, **kwargs):
        super(ProfileViewSet, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger(__name__)

    def retrieve(self, request, pk):
        try:
            user = TaggUser.objects.get(id=pk)

            if allow_to_view_private_content(request.user, user):
                response = {
                    "profile_pic": profile_pic_url(pk),
                    "header_pic": header_pic_url(pk),
                    "profile_info": get_profile_info_serialized(request.user, pk),
                    "moment_categories": get_moment_categories(user),
                    "linked_socials": get_linked_socials(pk),
                    "recent_moments": get_recent_moment_on_profile(user),
                }
            else:
                response = {
                    "profile_pic": profile_pic_url(pk),
                    "header_pic": header_pic_url(pk),
                    "profile_info": get_profile_info_serialized(request.user, pk),
                    "moment_categories": [],
                    "linked_socials": get_linked_socials(pk),
                }
            return Response(response)
        except TaggUser.DoesNotExist:
            return Response("User does not exist", status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            self.logger.exception(error)
            return Response(
                "Something went wrong", status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(detail=False, methods=["patch"])
    def tutorial(self, request):
        try:
            data = request.data
            if not "profile_tutorial_stage" in data:
                return Response("profile_tutorial_stage is required", 400)

            if (
                data["profile_tutorial_stage"]
                < ProfileTutorialStage.SHOW_TUTORIAL_VIDEOS
                or data["profile_tutorial_stage"] > ProfileTutorialStage.COMPLETE
            ):
                return Response("profile_tutorial_stage is invalid", 400)

            user = request.user
            user.taggusermeta.profile_tutorial_stage = data["profile_tutorial_stage"]
            user.save()
            return Response("Success")
        except Exception as error:
            logging.error(error)
            return Response("Something went wrong", 500)

# tma-2070 and tma-2031 Fetch tagg score for the user
class TaggScoreViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def __init__(self, *args, **kwargs):
        super(TaggScoreViewSet, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger(__name__)

    @action(detail=False, methods=["get"])
    def fetchTagScore(self, request):
        try:
            if "userId" not in request.query_params:
                return Response("userId is required", 400)
            user = request.query_params.get("userId")
            game_profile = GameProfile.objects.filter(tagg_user=user).first()
            currentScore = game_profile.tagg_score
            game_profile.tier = determine_gamification_tier(currentScore)
            game_profile.save()
            taggScore = game_profile.tagg_score
            taggTier = game_profile.tier
            data = {
                "tagg_coins": taggScore,
                "tagg_tier": taggTier,
            }
            return Response(data, 200)
        except TaggTierException as err:
            logging.error(
                "There was a problem in updating tier for user"
            )
            return Response(
                "There was a problem in updating tier for user",
                500
            )
        except Exception as err:
            logging.error(f'There was an error while fetching tagg Score: {err}')
            return Response('There was an error while fetching tagg Score')
        
from django.db.models.functions import Concat
from django.db.models import CharField, Value as V
class LeaderBoardViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = LeaderBoardSerializer

    def __init__(self, *args, **kwargs):
        super(LeaderBoardViewSet, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger(__name__)
        
    
    @action(detail=False, methods=["get"])
    def fetchLeaderboard(self, request):
        game_profile = GameProfile.objects.all().annotate(name=Concat('tagg_user__first_name', V(' ') ,'tagg_user__last_name')).values('name', 'today_score', 'tier', 'tagg_user__tier_icon',  "tagg_user__image_background", "tagg_user__color", "tagg_user_id", "tagg_user__username")

               
        game_profile_data = game_profile.order_by('-today_score').filter(today_score__gt=0)[:10]
        
        if not game_profile_data:
            return Response({"Message":"No Data Available"})
        
        
        res= LeaderBoardSerializer(game_profile_data, many=True)
        return Response(res.data, 200)


class LeaderboardProfileViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def __init__(self, *args, **kwargs):
        super(LeaderboardProfileViewSet, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger(__name__)

    @action(detail=False, methods=["get"])
    def LeaderboardProfile(self, request):
        try:
            if "userId" not in request.query_params:
                return Response("userId is required", 400)
            user = request.query_params.get("userId")
            game_profile = GameProfile.objects.filter(tagg_user=user).first()
            
            if not game_profile:
                return Response("User does not exist. ", 400)
            
            todayScore = game_profile.today_score
            users = game_profile.tagg_user
            username= str(users)
            game_profile.save()
            data = {
                "today_score": todayScore,
                "user_id":user,
                "profile":profile_pic_url(user),
                "username": username,
            }
            return Response(data, 200) 
        
        except Exception as err:
            logging.error(f'There was an error while fetching today Score: {err}')
            return Response('There was an error while fetching today Score')
        
        