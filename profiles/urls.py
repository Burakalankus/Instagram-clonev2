from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('<username>/', views.UserProfile, name='userProfile'),
]
