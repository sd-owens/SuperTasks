from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import Error
from django.views.generic import CreateView

from .models import Project, Feature, Subtasks
from .forms import ProjectForm, FeatureForm, SubtaskForm, UpdateSubtaskStatusForm, UpdateProjectForm, UpdateFeatureForm
from teams.models import Team
from accounts.models import Account

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

###
### CREATE A NEW SUBTASK FOR A FEATURE
###
@login_required
def new_subtask_view(request, project_id, feature_id):
    if request.method == 'GET':
        
        form = SubtaskForm(project_id)
        context = {'form': form,
                    "p_id": project_id
                }
        return render(request, 'projects/new_subtask.html', context)

    if request.method == "POST":
        form = SubtaskForm(project_id, request.POST)

        if not form.is_valid():
            # if form not valid, re-render form
            form = SubtaskForm(project_id)
            context = {'form': form}
            return render(request, 'projects/new_subtask.html', context)

        # if form is valid, get data and create subtask
        name = request.POST["name"]
        comment = request.POST["comment"]
        due_date = request.POST["due_date"]

        tasker_id = request.POST["tasker"]
        tasker = Account.objects.get(id=tasker_id)

        feature = Feature.objects.get(id=feature_id)

        try:
            Subtasks.objects.create(name=name, comment=comment, tasker=tasker, feature=feature, due_date=due_date)
            return redirect("projects_detail", project_id)
        except Error as err:
            context = {'error': str(err), 'form': form}
            return render(request, 'projects/new_subtask.html', context)

    # Return HTTP 405 Method Not Allowed
    return HttpResponseNotAllowed(['POST', 'GET'])

###
### UPDATE SUBTASK STATUS
###
@login_required
def update_subtask_status(request, project_id, feature_id, subtask_id):
    #get subtask
    subtask = Subtasks.objects.get(id=subtask_id)

    if request.method == "GET":
        form = UpdateSubtaskStatusForm(instance=subtask)

        context = {
            "subtask": subtask,
            "form": form,
        }

        #render update_subtask_status form
        return render(request, "projects/update_subtask_status.html", context)

    if request.method == "POST":
        form = UpdateSubtaskStatusForm(request.POST, instance=subtask)

        if form.is_valid():
            # if form is valid, save updates
            form.save()
            return redirect("projects_detail", project_id)
        else:
            #otherwise re render form
            form = UpdateSubtaskStatusForm(instance=subtask)

            context = {
                "subtask": subtask,
                "form": form,
            }

            #render update_subtask_status form
            return render(request, "projects/update_subtask_status.html", context)

    # Return HTTP 405 Method Not Allowed
    return HttpResponseNotAllowed(['POST', 'GET'])

@login_required
def new_feature_view(request, project_id):
    if request.method == 'GET':
        context = {'form': FeatureForm(),
                    "p_id": project_id
                    }
        return render(request, 'projects/new_feature.html', context)

    if request.method == 'POST':
        form = FeatureForm(request.POST)

        if not form.is_valid():
            context = {'form':form}
            return render(request, 'projects/new_feature.html', context)

        name = request.POST['name']
        description = request.POST['description']
        due_date = request.POST['due_date']
        priority = request.POST['priority']
        #project = request.POST['project']
        project = Project.objects.get(id=project_id)

        try:
            Feature.objects.create(
                name=name, 
                description=description, 
                due_date=due_date,
                priority=priority, 
                project=project,
                assignee_id=None
            )
            return redirect("projects_detail", project_id)
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

    sorted_f = data_p.feature_set.order_by('priority')

    context = {
        "project_data": data_p,
        "sorted_features": sorted_f,
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

###
### UPDATE AN EXISTING PROJECT
###
def update_project_view(request, project_id):
    project = Project.objects.get(id=project_id)

    if request.method == "GET":
        form = UpdateProjectForm(instance=project)

        context = {
            "project": project,
            "form": form,
        }

        return render(request, "projects/update_project.html", context)

    if request.method == "POST":
        form = UpdateProjectForm(request.POST, instance=project)

        if form.is_valid():
            form.save()
            return redirect("projects_detail", project_id)
        else:
            context = {
                "project": project,
                "form": form,
            }

            return render(request, "projects/update_project.html", context)

    # Return HTTP 405 Method Not Allowed
    return HttpResponseNotAllowed(['POST', 'GET'])

###
### UPDATE AN EXISTING FEATURE
###
def update_feature_view(request, project_id, feature_id):
    feature = Feature.objects.get(id=feature_id)

    if request.method == "GET":
        form = UpdateFeatureForm(instance=feature)

        context = {
            "feature": feature,
            "form": form 
        }

        return render(request, "projects/update_feature.html", context)

    if request.method == "POST":
        form = UpdateFeatureForm(request.POST, instance=feature)

        if form.is_valid():
            form.save()
            return redirect("projects_detail", project_id)
        else:
            form = UpdateFeatureForm(instance=feature)

            context = {
                "feature": feature,
                "form": form
            }

            return render(request, "projects/update_feature.html", context)

    # Return HTTP 405 Method Not Allowed
    return HttpResponseNotAllowed(['POST', 'GET'])
