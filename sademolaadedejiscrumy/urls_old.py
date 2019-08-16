from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views_old

app_name = 'sademolaadedejiscrumy'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login', auth_views.LoginView.as_view(), name='login'),
    path('', views_old.index, name='index'),
    path('movegoal/<int:goal_id>', views_old.move_goal, name='move_goal'),
    path('addgoal/', views_old.add_goal, name='add_goal'),
    path('home/', views_old.home, name='home'),
]