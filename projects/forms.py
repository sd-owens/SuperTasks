from django.forms import modelform_factory
from .models import Project, Feature, Subtasks
from django.forms import modelform_factory, ModelForm
from django import forms
from .models import Project, Feature, Subtasks
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
    
class UpdateProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ("name", "description", "start_date", "due_date", "budget", "status")



FeatureForm = modelform_factory(
    Feature,
    fields=("name", "description", "due_date"),
)

# SubtaskForm = modelform_factory(
#     Subtasks,
#     fields=("name", "comment", "due_date"),
# )

class UpdateFeatureForm(ModelForm):
    class Meta:
        model = Feature
        fields = ("name", "description", "status", "due_date")


class SubtaskForm(ModelForm):
    class Meta:
        model = Subtasks
        fields = ("name", "comment", "tasker", "due_date")

    def __init__(self, project_id, *args, **kwargs):
        super(SubtaskForm, self).__init__(*args, **kwargs)

        project_team = Project.objects.get(id=project_id).project_team #get the project

        self.fields["tasker"] = forms.ModelChoiceField(
            queryset=project_team.accounts.all()
        )

class UpdateSubtaskStatusForm(ModelForm):
    class Meta:
        model = Subtasks
        fields = ("status",)
