from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import Error
from django.views.generic import CreateView

from .models import Project, Feature, Subtasks
from teams.models import Team
from .forms import ProjectForm, FeatureForm, SubtaskForm
#from .serializers import ProjectSerializer

# Create your views here.
# done test view
def done_view(request, project_id):
    data_p = Project.objects.get(id=project_id)

    context = {
        "project_data": data_p
    }
    #Return to all projects page
    if request.method == 'POST':
        return HttpResponseRedirect('/projects/')
    return render(request, "projects/done_test.html", context)

# done test view (no features done)
def done2_view(request, project_id):
    data_p = Project.objects.get(id=project_id)

    context = {
        "project_data": data_p
    }
    #Return to all projects page
    if request.method == 'POST':
        return HttpResponseRedirect('/projects/')
    return render(request, "projects/done_test2.html", context)

@login_required
def feature_view(request):
    data_f = Feature.objects.all()

    context = {
        "feature_data": data_f
    }
    return render(request, "projects/project.html", context)

@login_required
def new_subtask_view(request, project_id, feature_id):
    if request.method == 'GET':
        context = {'form': SubtaskForm()}
        return render(request, 'projects/new_subtask.html', context)

    # Return HTTP 405 Method Not Allowed
    return HttpResponseNotAllowed(['POST', 'GET'])

@login_required
def new_feature_view(request, project_id):
    if request.method == 'GET':
        context = {'form': FeatureForm()}
        return render(request, 'projects/new_feature.html', context)

    if request.method == 'POST':
        form = FeatureForm(request.POST)

        if not form.is_valid():
            context = {'form':form}
            return render(request, 'projects/new_feature.html', context)

        name = request.POST['name']
        description = request.POST['description']
        due_date = request.POST['due_date']
        #project = request.POST['project']
        project = Project.objects.get(id=project_id)

        try:
            Feature.objects.create(
                name=name, 
                description=description, 
                due_date=due_date, 
                project=project,
                assignee_id=None
            )
            return HttpResponseRedirect('/projects')
        except Error as err:
            context = {'error': str(err), 'form':form}
            return render(request, 'projects/new_feature.html', context)

    # Return HTTP 405 Method Not Allowed
    return HttpResponseNotAllowed(['POST', 'GET'])

@login_required
def project_view(request):
    #get teams the user is a member of
    user_teams = request.user.account.team_set.all()

    #get project the user is working on
    user_projects = Project.objects.filter(project_team__in=user_teams)

    context = {
        "project_data": user_projects,
    }
    return render(request, "projects/projects.html", context)

@login_required
def detail_project_view(request, project_id):
    data_p = Project.objects.get(id=project_id)

    context = {
        "project_data": data_p,
    }
    if request.method == 'POST':
        has_feature = data_p.set_to_done()
        if has_feature:
            # Check redirect to done page temporarily
            return HttpResponseRedirect('/projects/done/'+str(project_id))
        else:
            return HttpResponseRedirect('/projects/done2/'+str(project_id))
    return render(request, 'projects/project_edit.html', context)


@login_required
def new_project_view(request):
    if request.method == 'GET':
        form = ProjectForm(request.user) #create form
        teams = request.user.account.team_set.all() # query all teams user is on

        context = {
            'form': form,
            "teams": teams,
        }
        return render(request, 'projects/new_project.html', context)

    if request.method == 'POST':
        form = ProjectForm(request.user, request.POST)
        
        if not form.is_valid():
            print(form.errors)
            form = ProjectForm(request.user)  # create form
            teams = request.user.account.team_set.all()  # query all teams user is on

            context = {
                'form': form,
                "teams": teams,
            }
            # put the error message in here
            return render(request, 'projects/new_project.html', context)

        name = request.POST['name']
        description = request.POST['description']
        start_date = request.POST['start_date']
        due_date = request.POST['due_date']
        budget = request.POST['budget']
        team_id = request.POST["project_team"]
        project_team = Team.objects.get(id=team_id)

        try:
            Project.objects.create(name=name, description=description,
                                   start_date=start_date, due_date=due_date, 
                                   budget=budget, project_team=project_team)

            # Check where this redirects
            return HttpResponseRedirect('/projects')
        except Error as err:
            context = {'error': str(err), 'form':form}
            return render(request, 'projects/new_project.html', context)

    # Return HTTP 405 Method Not Allowed
    return HttpResponseNotAllowed(['POST', 'GET'])
