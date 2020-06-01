#from rest_framework import serializers
from .models import Project

"""
class ProjectSerializer(serializers, ModelSerializer):
    class meta:
        model = Project
        fields = ['name', 'description', 'start_date'. 'due_date', 'budget', 'status', 'project_team']
