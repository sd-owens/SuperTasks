# Overall project views, apps have their own views.py file.

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    context = {}  # reserved for later use in rendering home

    return render(request, 'index.html', context)
