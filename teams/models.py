from django.db import models

# Create your models here.

class Team(models.Model):

    team_name = models.CharField(max_length=50)
    users = models.ManyToManyField("accounts.Account")
    task = models.ForeignKey("projects.Feature", on_delete=models.CASCADE, blank = True, null = True)
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.team_name