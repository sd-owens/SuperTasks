from django.http import HttpResponseRedirect, HttpResponseNotAllowed, HttpResponseNotFound
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import Error

from accounts.models import Account
from .models import Team
from .forms import TeamForm


@login_required
def dashboard_view(request):
    "Displays a list of the existing teams and their members. URL: /teams"
    #get teams the user is a member of
    user_teams = request.user.account.team_set.all()

    context = {'teams': user_teams}
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
        print(member_ids)
        context = {
            'form': TeamForm(instance=team),
            'accounts': accounts,
            'is_new_team': False,
            'member_ids': member_ids,
        }
        return render(request, "teams/team.html", context)

    #TODO this method is not standard REST, needs converted to PUT at future time.
    if request.method == 'POST':

        try:

            # create "set" of accounts to be added or removed
            edit_accounts = set(request.POST.getlist('accounts'))

            # existing team and team accounts
            team = Team.objects.get(id=team_id)
          
            # create "set" of original accounts that exist in current team
            orig_accounts = set([str(account.id) for account in team.accounts.all()])

            # add accounts is the set difference of edit and original accounts
            add_accounts = edit_accounts - orig_accounts

            # remove accounts is the set set difference of original and edit accounts
            remove_accounts = orig_accounts - edit_accounts

            # iterate through the union of the two sets for each account_id
            for account_id in add_accounts:

                team.accounts.add(account_id)

            for account_id in remove_accounts:
                
                team.accounts.remove(account_id)

            return HttpResponseRedirect('/teams')

        #TODO this error does not redirect to correct location for failure to update a team.
        except Error as err:

            context = {'error': str(err), 'form': form}
            return render(request, 'teams/new_team.html', context)

    # Return HTTP 405 Method Not Allowed
    return HttpResponseNotAllowed(['POST', 'GET'])
