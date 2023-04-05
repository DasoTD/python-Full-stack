from django.db import models
import string
import random
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

# Create your models here.
def unique_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Rum.objects.filter(code=code).count() == 0:
            break
    return code


class Rum(models.Model):
    code = models.CharField(max_length=8, unique=True, default=unique_code)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip= models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

class Data(models.Model):
    data: models.CharField(max_length=20)

User = get_user_model()

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-image.jpg')
    location = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default= datetime.now)
    no_of_likes = models.IntegerField(default=0)

    
    def __str__(self):
        return self.user
