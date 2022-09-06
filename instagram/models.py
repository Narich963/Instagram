from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):

    name  = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to='avatars/')
    description = models.TextField(blank=True, null=True)
    followers = models.IntegerField(default=0)
    followed = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('detail', args=[
            self.pk,
        ])



class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')
    comment = models.CharField(max_length=250, blank=True, null=True, default='')
    publish_date = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0)
    is_liked = models.BooleanField(default=False)






