from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""
Account model 
"""
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    profile_picture = models.ImageField(
        default="default-profile-picture.jpg", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
