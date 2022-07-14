from rest_framework import serializers
from datetime import datetime
from ..serializers import TaggUserSerializer
from .models import GameProfile, Feature, UserFeature
from ..common.image_manager import leaderboard_pic_url


class GameProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = GameProfile
        fields = ["user", "tagg_score", "tier", "rewards", "newRewardsReceived"]

    def get_user(self, obj):
        return TaggUserSerializer(obj.tagg_user).data
    
class LeaderBoardSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    tier_icon = serializers.SerializerMethodField()
    profile_image = serializers.SerializerMethodField()
    image_background = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    class Meta:
        model = GameProfile
        fields = ["tagg_score", "tier", "rewards", "today_score", 'name', "newRewardsReceived", "tier_icon", "profile_image", "image_background", "color", "username", "user_id"]
        
    def get_name(self, obj):
        return f"{obj['name']}"
    
    def get_tier_icon(self, obj):
        return f"/mediafiles/{obj['tagg_user__tier_icon']}"
    
    def get_profile_image(self, obj):
        return leaderboard_pic_url(obj['tagg_user_id'])
    
    def get_image_background(self, obj):
        return f"/mediafiles/{obj['tagg_user__image_background']}"
    
    def get_color(self, obj):
        return f"{obj['tagg_user__color']}"
    
    def get_username(self, obj):
        return f"{obj['tagg_user__username']}"
    
    def get_user_id(self, obj):
        return f"{obj['tagg_user_id']}"

class FeatureSerializer(serializers.ModelSerializer):
    unlocked = serializers.BooleanField(default=False)

    class Meta:
        model = Feature
        fields = "__all__"
        extra_fields = ["unlocked"]


class UserFeatureSerializer(serializers.ModelSerializer):
    feature = serializers.SerializerMethodField()

    class Meta:
        model = UserFeature
        fields = "__all__"

    def get_feature(self, user_feature):
        feature = user_feature.feature
        feature.unlocked = True
        return FeatureSerializer(feature).data


class UserFeatureCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFeature
        fields = ("user", "feature", "active")
