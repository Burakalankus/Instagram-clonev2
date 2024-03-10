from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import Paginator
from .models import Profile
from post.models import Post
from .models import Follow
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def UserProfile(request, username):
    profile_user = get_object_or_404(User, username=username)
    profile, created = Profile.objects.get_or_create(user=profile_user)

    posts = Post.objects.filter(created_by=profile_user).order_by('-created_at')
    posts_count = posts.count()
    following_count = Follow.objects.filter(follower=profile_user).count()
    followers_count = Follow.objects.filter(following=profile_user).count()
    follow_status = Follow.objects.filter(following=profile_user, follower=request.user).exists()

    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    posts_paginator = paginator.get_page(page_number)
    
   
    context = {
        'profile_user': profile_user,
        'profile': profile,
        'posts_count': posts_count,
        'following_count': following_count,
        'followers_count': followers_count,
        'posts_paginator': posts_paginator,
        'follow_status': follow_status,
       
    }
    return render(request, 'pages/profile.html', context)


@login_required
def follow_user(request, username):
    following_user = User.objects.get(username=username)
    Follow.objects.get_or_create(follower=request.user, following=following_user)
    referer_url = request.META.get('HTTP_REFERER')
    return redirect(referer_url)

@login_required
def unfollow_user(request, username):
    following_user = User.objects.get(username=username)
    Follow.objects.filter(follower=request.user, following=following_user).delete()
    referer_url = request.META.get('HTTP_REFERER')
    return redirect(referer_url)
