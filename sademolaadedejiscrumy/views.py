from rest_framework import viewsets
from sademolaadedejiscrumy.serializers import UserSerializer, ScrumyGoalsSerializer, ScrumyHistorySerializer, GoalStatusSerializer
from django.contrib.auth.models import User
from .models import ScrumyGoals, ScrumyHistory, GoalStatus

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ScrumyGoalsSet(viewsets.ModelViewSet):
    """
    API endpoint that allows scrumygoals to be viewed or edited.
    """
    queryset = ScrumyGoals.objects.all()
    serializer_class = ScrumyGoalsSerializer

class ScrumyHistorySet(viewsets.ModelViewSet):
    """
    API endpoint that allows scrumyhistorys to be viewed or edited.
    """
    queryset = ScrumyHistory.objects.all()
    serializer_class = ScrumyHistorySerializer

class GoalStatusSet(viewsets.ModelViewSet):
    """
    API endpoint that allows goalstatuses to be viewed or edited.
    """
    queryset = GoalStatus.objects.all()
    serializer_class = GoalStatusSerializer