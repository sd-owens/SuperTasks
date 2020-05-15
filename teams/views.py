from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import Error

from accounts.models import Account
from .models import Team
from .forms import TeamForm


@login_required
def team_view(request):
    context = {}
    return render(request, "teams/team.html", context)


@login_required
def new_team_view(request):
    if request.method == 'GET':
        accounts = Account.objects.all()

        context = {'form': TeamForm(), 'accounts': accounts}
        return render(request, "teams/new_team.html", context)

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
