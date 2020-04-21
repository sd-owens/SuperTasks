# Overall project views, apps have their own views.py file.

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {}  # reserved for later use in rendering home
    return render(request, 'index.html', context)