from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_pics', default='profile_pics/default.jpg', blank=True)
    bio = models.TextField(max_length=300, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    follower_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)  

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    def get_profile_image_url(self):
        if self.profile_image and hasattr(self.profile_image, 'url'):
            return self.profile_image.url
        return  'https://picsum.photos/id/64/30/30'

    def __str__(self):
        return f'{self.user.username} Profile'


from django.contrib.auth.models import User
from django.db import models

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f"{self.follower.username} is following {self.following.username}"
