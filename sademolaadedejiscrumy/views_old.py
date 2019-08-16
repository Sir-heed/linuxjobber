from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.urls import reverse

from random import choice

from .models import GoalStatus, ScrumyGoals, ScrumyHistory
from .forms import SignupForm, CreateGoalForm, MoveGoalForm
# Create your views here.

def index(request):
    # return HttpResponse("Hello World.")
    # goal = ScrumyGoals.objects.filter(goal_name="Learn Django")
    # return HttpResponse(goal)

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
            user = User.objects.get(username=username)
            dev_group = Group.objects.get(name='Developer')
            dev_group.user_set.add(user)
            return HttpResponse('<h1>Your account has been created successfully.<h1>')
    else:
        form = SignupForm()
    return render(request, 'sademolaadedejiscrumy/index.html', {'form':form})


def move_goal(request, goal_id):
    # try:
    #     goal = ScrumyGoals.objects.get(goal_id=goal_id)
    # except ScrumyGoals.DoesNotExist:
    #     context = {
    #         'error':'A record with a goal id of %s does not exist.' % goal_id
    #     }
    #     return render(request, 'sademolaadedejiscrumy/exception.html', context=context)
    # return HttpResponse(goal)
    try:
        goal = ScrumyGoals.objects.get(goal_id=goal_id)
        if request.method == 'POST':
            form = MoveGoalForm(request.POST)
            if form.is_valid(): 
                user = request.user
                status = form.cleaned_data['goal_status']
                developer = Group.objects.get(name='Developer')
                admin = Group.objects.get(name='Admin')
                quality_assurance = Group.objects.get(name='Quality Assurance')
                owner = Group.objects.get(name='Owner')
                # Developers Condition
                if (developer in request.user.groups.all()) & (status != 'Done Goal') & (goal.user == user):
                    goal.goal_status = GoalStatus.objects.get(status_name=status)
                    goal.save()
                    # return HttpResponse('<h1>Your goal status has been changed successfully.</h1>')
                    return HttpResponseRedirect(reverse('sademolaadedejiscrumy:home'))
                # elif (developer in request.user.groups.all()) & (status == 'Done Goal') & (goal.user == user):
                #     # return HttpResponse('<h1>You cannot move your goal to Done Goal</h1>')
                #     return HttpResponseRedirect(reverse('sademolaadedejiscrumy:home'))
                # else:
                    # return HttpResponse('<h1>You are not authorised to move this goal.</h1>')
                    # return HttpResponseRedirect(reverse('sademolaadedejiscrumy:home'))

                # Quality Assurance Condition
                elif (quality_assurance in request.user.groups.all()) & (goal.user == user):
                    goal.goal_status = GoalStatus.objects.get(status_name=status)
                    goal.save()
                    # return HttpResponse('<h1>Your goal status has been changed successfully.</h1>')
                    return HttpResponseRedirect(reverse('sademolaadedejiscrumy:home'))
                elif (quality_assurance in request.user.groups.all()) & (goal.goal_status == 'Verify Goal') & (goal.user != user):
                    if status == 'Done Goal':
                        goal.goal_status = GoalStatus.objects.get(status_name=status)
                        goal.save()
                        # return HttpResponse('<h1>The goal status has been changed successfully.</h1>')
                        return HttpResponseRedirect(reverse('sademolaadedejiscrumy:home'))
                    else:
                        # return HttpResponse('<h1>You are not authorised to move this goal.</h1>')
                        return HttpResponseRedirect(reverse('sademolaadedejiscrumy:home'))
                # else:
                #     # return HttpResponse('<h1>You are not authorised to move this goal.</h1>')
                #     return HttpResponseRedirect(reverse('sademolaadedejiscrumy:home'))

                # Admin condtion
                elif admin in request.user.groups.all():
                    goal.goal_status = GoalStatus.objects.get(status_name=status)
                    goal.save()
                    # return HttpResponse('<h1>The goal status has been changed successfully.</h1>')
                    return HttpResponseRedirect(reverse('sademolaadedejiscrumy:home'))

                # Owner condition
                elif (owner in request.user.groups.all()) & (goal.user == user):
                    goal.goal_status = GoalStatus.objects.get(status_name=status)
                    goal.save()
                    # return HttpResponse('<h1>Your goal status has been changed successfully.</h1>')
                    return HttpResponseRedirect(reverse('sademolaadedejiscrumy:home'))
                else:
                    # return HttpResponse('<h1>You are not authorised to move this goal.</h1>')
                    # return HttpResponseRedirect(reverse('sademolaadedejiscrumy:home'))
                    return render(request, 'sademolaadedejiscrumy/invalid.html')
        else:
            form = MoveGoalForm()
        return render(request, 'sademolaadedejiscrumy/movegoal.html', {'form':form})
    except ScrumyGoals.DoesNotExist:
        context = {
            'error':'A record with a goal id of %s does not exist.' % goal_id
        }
        return render(request, 'sademolaadedejiscrumy/exception.html', context=context)


def add_goal(request):
    # all_ids = [i.goal_id for i in ScrumyGoals.objects.all()]
    # new_id = choice([i for i in range(1001,9999) if i not in all_ids])
    # new_goal = ScrumyGoals(goal_name='Keep Learning Django', goal_id=new_id, created_by='Louis', moved_by='Louis', owner='Louis')
    # new_goal.goal_status = GoalStatus.objects.get(status_name='Weekly Goal')
    # new_goal.user = User.objects.get(username='louis')
    # new_goal.save()
    # return HttpResponse(new_goal)

    if request.method == 'POST':
        form = CreateGoalForm(request.POST)
        if form.is_valid():
            form.save()
            goal_name = form.cleaned_data['goal_name']
            goal = ScrumyGoals.objects.get(goal_name=goal_name)
            goal.goal_status = GoalStatus.objects.get(status_name='Weekly Goal')
            goal.save()
            return HttpResponseRedirect(reverse('sademolaadedejiscrumy:home'))
    else:
        form = CreateGoalForm()
    return render(request, 'sademolaadedejiscrumy/addgoal.html', {'form':form})

def home(request):
    # goals = ScrumyGoals.objects.filter(goal_name='Keep Learning Django')
    # output = ', '.join([i.goal_name for i in goals])
    # return HttpResponse(output)

    # goal = ScrumyGoals.objects.get(pk=1)
    # context = {
    #     'goal_name': goal.goal_name,
    #     'goal_id': goal.goal_id,
    #     'user': User.objects.get(username=goal.user)
    # }
    # return render(request, 'sademolaadedejiscrumy/home.html', context=context)

    context = {
        'user': request.user,
        'users': User.objects.all(),
        'weekly_goals': GoalStatus.objects.get(status_name='Weekly Goal').scrumygoals_set.all(),
        'daily_goals': GoalStatus.objects.get(status_name='Daily Goal').scrumygoals_set.all(),
        'verify_goals': GoalStatus.objects.get(status_name='Verify Goal').scrumygoals_set.all(),
        'done_goals': GoalStatus.objects.get(status_name='Done Goal').scrumygoals_set.all()
    }
    return render(request, 'sademolaadedejiscrumy/home.html', context=context)