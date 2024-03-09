import os
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils.timesince import timesince
from django.utils import timezone
from center import settings
from profiles.models import Profile

class Post(models.Model):
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    caption = models.TextField(max_length=1000, blank=True)
    likes = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=100, blank=True)
    uuid = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)

    def __str__(self):
        return f"Post {self.uuid}"
    

class Comment(models.Model):
    content = models.CharField(max_length=200, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Comment on {self.post}"

    class Meta:
        ordering = ['-created']

    @property
    def time_diff(self):
        now = timezone.now()
        diff = now - self.created
        if diff.days > 0:
            return f"{diff.days} days ago"
        elif diff.seconds // 3600 > 0:
            return f"{diff.seconds // 3600} hours ago"
        elif diff.seconds // 60 > 0:
            return f"{diff.seconds // 60} minutes ago"
        else:
            return "Just now"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f'{self.user} likes {self.post}'

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
class Follower(models.Model):
    follower = models.ForeignKey(User, related_name='following_set', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers_set', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower', 'following')