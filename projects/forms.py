from django.forms import modelform_factory
from .models import Project

# Automatically creates a form from the model
ProjectForm = modelform_factory(
    Project,
    fields=("name", "description", "start_date", "due_date", "budget"),
)
