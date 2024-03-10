from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('<username>/', views.UserProfile, name='userProfile'),
    path('<str:username>/follow/', views.follow_user, name='follow'),
    path('<str:username>/unfollow/', views.unfollow_user, name='unfollow'),
]
