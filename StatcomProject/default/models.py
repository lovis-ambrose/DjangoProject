from distutils.command import upload
from email.policy import default
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    pp = models.ImageField(upload_to = "profiles", blank = True, null = True, default = "/profiles/default.jpg")
    # attach relationship 
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_(self):
        return str(self.owner)
class Gallery(models.Model):
    pic = models.ImageField(upload_to = "gallery", blank = True, null = True, default = "/gallery/default.jpg")
    caption = models.TextField(max_length=300, default="", blank=True, null=True)
    def __str__(self):
        return str(self.caption)