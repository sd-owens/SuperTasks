from datetime import date
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

    def __str__(self):
        return self.name

    # Basic data type fields
    name = models.CharField(max_length=256)
    description = models.TextField()
    start_date = models.DateField(default=date.today)
    due_date = models.DateField()
    budget = models.FloatField(default=0)

    class ProjectStatus(models.IntegerChoices):
        "Enum to save as the project status"
        NOT_STARTED = 0
        IN_PROGRESS = 10
        UNDER_REVIEW = 20
        COMPLETED = 30
        STALLED = 40

    status = models.IntegerField(choices=ProjectStatus.choices, default=ProjectStatus.NOT_STARTED)


    # Relational fields
    # Feature model will have a FK to the Project model
    
    # leader = models.ForeignKey(
    #    User,
    #    on_delete=models.CASCADE,
    #    related_name='project_leader',
    #)
    
    members = models.ManyToManyField(User)

    def is_overdue(self):
        "Returns True if today is greater than the Due Date and the project is not completed."
        today = date.today()
        return today > self.due_date and self.status != Project.ProjectStatus.COMPLETED

    def set_to_done(self):
        "Sets all the features associated with it to done, returns false if no features"
        self.status=Project.ProjectStatus.COMPLETED
        self.save()
        has_feature = False
        self.feature_set.all().update(status=Feature.FeatureStatus.DONE)
        if (self.feature_set.all().count() > 0):
            has_feature = True
        return has_feature
        

    # Below are examples of optional fields that could be added
    # for future user stories if necessary
    # client
    # milestones
    # to-do items

# Create your models here. 
#TODO create an add feature button to the projects page.
class Feature(models.Model):
    """Model describing a Feature

    For a Feature has a foreign key
    to the Project - each Feature has one project it is under.

    For a Feature has a foreign key
    to the User - each Feature has one assigned user.
    """

    # Basic data type fields
    title = models.TextField()
    name = models.CharField(max_length=256)
    description = models.TextField()
    due_date = models.DateField()


    class FeatureStatus(models.IntegerChoices):
        "Enum to save as the feature status"
        TO_DO = 0
        IN_PROGRESS = 10
        DONE = 20

    status = models.IntegerField(choices=FeatureStatus.choices, default=FeatureStatus.TO_DO)


    # Relational fields
    # Feature model will have a FK to the Project model and User model
    
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    assignee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='assigned_user'
    )

