from django.http import HttpResponseRedirect, HttpResponseNotAllowed, HttpResponseNotFound
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import Error

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.models import Account
from .models import Team
from .forms import TeamForm


@login_required
def dashboard_view(request):
    "Displays a list of the existing teams and their members. URL: /teams"
    teams = Team.objects.all()
    context = {'teams': teams}
    return render(request, "teams/dashboard.html", context)


@login_required
def new_team_view(request):
    "Displays a form to create a new team. URL: /teams/new"
    if request.method == 'GET':
        accounts = Account.objects.all()

        context = {'form': TeamForm(), 'accounts': accounts, 'is_new_team': True}
        return render(request, "teams/team.html", context)

    if request.method == 'POST':
        form = TeamForm(request.POST)

        if not form.is_valid():
            context = {'form': form}

            return render(request, 'teams/new_team.html', context)

        name = request.POST['name']
        accounts = request.POST.getlist('accounts')

        try:
            team = Team.objects.create(name=name)
            for account_id in accounts:
                team.accounts.add(account_id)
            # Check where this redirects
            return HttpResponseRedirect('/teams')
        except Error as err:
            context = {'error': str(err), 'form': form}
            return render(request, 'teams/new_team.html', context)

    # Return HTTP 405 Method Not Allowed
    return HttpResponseNotAllowed(['POST', 'GET'])

@api_view (['GET', 'PUT'])
@login_required
def team_view(request, team_id):
    "Displays an existing team and allows for editing. URL: /teams/<int:team_id>"
    if request.method == 'GET':
        # Get the Team object from the database
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return HttpResponseNotFound(f'404: Team {team_id} does not exist.')

        # Get a list of accounts to populate the choices in the HTML dropdown
        accounts = Account.objects.all()

        # Get a list of the member ids for pre-selecting the dropdown multi-select
        member_ids = [str(account.id) for account in team.accounts.all()]

        context = {
            'form': TeamForm(instance=team),
            'accounts': accounts,
            'is_new_team': False,
            'member_ids': member_ids,
        }
        print("test")
        return render(request, "teams/team.html", context)

    if request.method == 'PUT':
        # Replace with logic to update the existing team


        # name = request.PUT['name']


        # not reaching this line!!
        print("That was a PUT request")
        print(request.PUT)
        return HttpResponseRedirect('/')

    # Return HTTP 405 Method Not Allowed
    
    # Never makes it here also!!
    print("you are here")
    return HttpResponseNotAllowed(['POST', 'GET'])
