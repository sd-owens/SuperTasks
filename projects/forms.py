from django.forms import modelform_factory, ModelForm
from django import forms
from .models import Project, Feature
from teams.models import Team

#Automatically creates a form from the model
# ProjectForm = modelform_factory(
#     Project,
#     fields=("name", "description", "start_date", "due_date", "budget", "project_team"),
# )

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ("name", "description", "start_date", "due_date", "budget", "project_team")

    # ModelForm constructor adds project_team choice based off of the user requesting the form
    def __init__(self, user, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['project_team'] = forms.ModelChoiceField(
            queryset=user.account.team_set.all()
        )
    


FeatureForm = modelform_factory(
    Feature,
    fields=("name", "description", "due_date", "priority"),
)
