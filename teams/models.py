from django.db import models

# Create your models here.

class Team(models.Model):

    team_name = models.CharField(max_length=50)
    users = models.ManyToManyField("accounts.Account")
    tasks = models.ManyToManyField("projects.Feature")

    def __str__(self):
        return self.team_name