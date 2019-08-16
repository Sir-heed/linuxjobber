from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GoalStatus(models.Model):
    """This will store all possible status of a goal."""
    status_name = models.CharField(max_length=50)

    def __str__(self):
        return self.status_name

class ScrumyGoals(models.Model):
    """This will keep record of each goals"""
    goal_name = models.CharField(max_length=50)
    goal_id = models.AutoField(primary_key=True)
    created_by = models.CharField(max_length=50)
    moved_by = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    goal_status = models.ForeignKey(GoalStatus, on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')

    def __str__(self):
        return self.goal_name


class ScrumyHistory(models.Model):
    """This will store information about activities/actions carried out on a goal."""  
    moved_by = models.CharField(max_length=50)
    created_by = models.CharField(max_length=50)
    moved_from = models.CharField(max_length=50)
    moved_to = models.CharField(max_length=50)
    time_of_action = models.DateTimeField()
    goal = models.ForeignKey(ScrumyGoals, on_delete=models.CASCADE)

    def __str__(self):
        return self.time_of_action