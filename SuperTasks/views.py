# Overall project views, apps have their own views.py file.

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {}  # reserved for later use in rendering home

    # Checks session cookie if they are logged in or not
    if 'username' in request.session:
        context['username'] = request.session['username']
    return render(request, 'index.html', context)