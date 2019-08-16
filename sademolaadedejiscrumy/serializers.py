from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ScrumyGoals, GoalStatus, ScrumyHistory

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ScrumyGoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrumyGoals
        fields = ['goal_name', 'goal_id', 'created_by', 'moved_by', 'owner', 'goal_status', 'user']

class GoalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalStatus
        fields = ['status_name']

class ScrumyHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrumyHistory
        fields = ['moved_by', 'created_by', 'moved_from', 'moved_to', 'time_of_action', 'goal']
