from django.forms import modelform_factory
from .models import Team

# Automatically creates a form from the model
TeamForm = modelform_factory(
    Team,
    fields=("team_name", "users", "project"),  # a team can have a project or not upon creation
)
