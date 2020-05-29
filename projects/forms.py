from django.forms import modelform_factory
from .models import Project, Feature, Subtasks

# Automatically creates a form from the model
ProjectForm = modelform_factory(
    Project,
    fields=("name", "description", "start_date", "due_date", "budget"),
)

FeatureForm = modelform_factory(
    Feature,
    fields=("name", "description", "due_date"),
)

SubtaskForm = modelform_factory(
    Subtasks,
    fields=("name", "comment", "due_date"),
)