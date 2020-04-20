from django.db import models

# Create your models here.
class User(models.Model):
    """Database model representing a user

    Mandatory fields: username, email, password
    """

    username = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.username}({self.email})"
