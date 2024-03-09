from django.urls import path
from center import settings 
from post import views
from django.conf.urls.static import static
app_name = 'post'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('home/', views.index, name = 'home'),
    path('create_post/', views.create_post, name='create_post'),
    path('register/',views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('<uuid:uuid>/like/', views.like_view, name='like'),
    path('<uuid:uuid>/comment/', views.comment_view, name='comment'),
    path('explore/', views.explore_view, name='explore'),
]

