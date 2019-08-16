from django.forms import ModelForm
from django import forms

from .models import ScrumyGoals
from django.contrib.auth.models import User

class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

class CreateGoalForm(ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = ['goal_name', 'user']

STATUS = [
    ('Weekly Goal', 'Weekly Goal'),
    ('Daily Goal', 'Daily Goal'),
    ('Verify Goal', 'Verify Goal'),
    ('Done Goal', 'Done Goal')
]
class MoveGoalForm(forms.Form):
    goal_status = forms.CharField(widget=forms.Select(choices=STATUS))