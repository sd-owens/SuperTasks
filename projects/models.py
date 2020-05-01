from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    """Model describing a Project

    For a project leader, the Project has a foreign key
    to the User - each Project has one leader and a
    User can be the leader for many projects.

    For project members, there is a many-to-many relationship,
    a project has many members and a User can be a member
    of many projects.
    """

    # Basic data type fields
    name = models.CharField(max_length=256)
    description = models.TextField()
    due_date = models.DateField()
    start_date = models.DateField(default=datetime.now)
    budget = models.FloatField(default=0)

    class ProjectStatus(models.IntegerChoices):
        "Enum to save as the project status"
        NOT_STARTED = 0
        IN_PROGRESS = 10
        UNDER_REVIEW = 20
        COMPLETED = 30
        STALLED = 40

    status = models.IntegerField(choices=ProjectStatus.choices)


    # Relational fields
    # Feature model will have a FK to the Project model
    leader = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='project_leader'
    )
    members = models.ManyToManyField(User)

    # Below are examples of optional fields that could be added
    # for future user stories if necessary
    # client
    # milestones
    # to-do items
