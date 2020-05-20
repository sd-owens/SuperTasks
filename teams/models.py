from django.db import models

# Create your models here.

class Team(models.Model):

    name = models.CharField(max_length=50)
    accounts = models.ManyToManyField("accounts.Account", blank=True)
    projects = models.ManyToManyField("projects.Project", blank=True)

    def __str__(self):
        return self.name