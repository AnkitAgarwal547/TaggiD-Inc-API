from rest_framework import routers

from .api import ProfileViewSet, TaggScoreViewSet, LeaderBoardViewSet, LeaderboardProfileViewSet

router = routers.DefaultRouter()
router.register("api/profile", ProfileViewSet, "profile")
router.register("api/taggscore", TaggScoreViewSet, "taggscore")
router.register("api/leaderboard", LeaderBoardViewSet, "leaderboard")
router.register("api/leaderboard-profile", LeaderboardProfileViewSet, "leaderboard-profile")
urlpatterns = router.urls
