from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import Error

from .models import Project
from .forms import ProjectForm

# Create your views here.
# test view
@login_required
def project_view(request):
    context = {
        "message" : "welcome",
    }
    return render(request, "projects/test_template.html", context)

@login_required
def new_project_view(request):
    if request.method == 'GET':
        context = {'form': ProjectForm()}
        return render(request, 'projects/new_project.html', context)

    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if not form.is_valid():
            context = {'form':form}
            return render(request, 'accounts/register.html', context)

        name = request.POST['name']
        description = request.POST['description']
        start_date = request.POST['start_date']
        due_date = request.POST['due_date']
        budget = request.POST['budget']

        try:
            Project.objects.create(name=name, description=description,
                                   start_date=start_date, due_date=due_date, 
                                   budget=budget)
            return HttpResponseRedirect('/')
        except Error as err:
            context = {'error': str(err), 'form':form}
            return render(request, 'projects/new_project.html', context)

    # Return HTTP 405 Method Not Allowed
    return HttpResponseNotAllowed(['POST', 'GET'])
