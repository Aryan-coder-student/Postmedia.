from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime
# Create your models here.
# ----------------------------------------------------------------
class post_details(models.Model):
    id = models.UUIDField(primary_key=True,default =uuid.uuid4)
    user = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=100000)
    postImg = models.ImageField(upload_to="user_post_images/")
    timePosted = models.DateTimeField(default=datetime.now)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.user
    
# ----------------------------------------------------------------
class user_profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)                                        
    id_user = models.IntegerField()    
    bio = models.TextField(max_length=2000)
    prof_img = models.ImageField(upload_to="user_profile/",default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsUNceR8jbqHa2R3491RxiE8Nmcy8PHiFLTfF_OQ6xng&s')
    status = models.CharField(max_length=2000)      
    def __str__(self):
        return self.user.username
# ----------------------------------------------------------------
class likePost(models.Model):
    post_id = models.CharField(max_length=300)
    username = models.CharField(max_length=300)
    def __str__(self):
        return self.username
# ----------------------------------------------------------------
class follower(models.Model):
    user_to_whom = models.CharField(max_length=2000)
    user_who_follow = models.CharField(max_length=2000)
    def __str__(self):
        return self.user_to_whom
    