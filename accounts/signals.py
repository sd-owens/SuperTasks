from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Account

"""
Signal runs everytime a new user is created and creates a new account linked to the user
"""
@receiver(post_save, sender=User)
def create_profile_for_user(sender, instance, created, **kwargs):
    if created:
        username = instance.username
        email = instance.email

        Account.objects.create(user=instance, username=username, email=email)
        print("New User registered and Account created.") 
