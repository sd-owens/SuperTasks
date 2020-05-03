from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import Error

from .models import Project, Feature
from .forms import ProjectForm

# Create your views here.
# feature test view
@login_required
def feature_view(request):
    data = Feature.objects.all()

    context = {
        "feature_data": data
    }
    return render(request, "projects/features.html", context)
    #return render_to_response("login/profile.html", context)

@login_required
def project_view(request):
    data = Project.objects.all()

    context = {
        "project_data": data
    }
    return render(request, "projects/projects.html", context)
    #return render_to_response("login/profile.html", context)

@login_required
def new_project_view(request):
    if request.method == 'GET':
        context = {'form': ProjectForm()}
        return render(request, 'projects/new_project.html', context)

    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if not form.is_valid():
            context = {'form':form}
            # put the error message in here
            return render(request, 'accounts/new_project.html', context)

        name = request.POST['name']
        description = request.POST['description']
        start_date = request.POST['start_date']
        due_date = request.POST['due_date']
        budget = request.POST['budget']

        try:
            Project.objects.create(name=name, description=description,
                                   start_date=start_date, due_date=due_date, 
                                   budget=budget)
            # Check where this redirects
            return HttpResponseRedirect('/projects')
        except Error as err:
            context = {'error': str(err), 'form':form}
            return render(request, 'projects/new_project.html', context)

    # Return HTTP 405 Method Not Allowed
    return HttpResponseNotAllowed(['POST', 'GET'])
