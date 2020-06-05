from django.contrib import admin
from .models import Project, Feature, Subtasks

# Register your models here.
admin.site.register(Project)
admin.site.register(Feature)
admin.site.register(Subtasks)
