from django.forms import modelform_factory
from .models import Team

# Automatically creates a form from the model
TeamForm = modelform_factory(
    Team,
    fields=("name", "users", "projects"),  # a team can have a project or not upon creation
)
