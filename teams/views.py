from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import Error

# Create your views here.

@login_required
def team_view(request):


    context = {}
    return render(request, "teams/team.html", context)

#TODO new team 
#@login_required
#def new_team_view(request):

   # return ren