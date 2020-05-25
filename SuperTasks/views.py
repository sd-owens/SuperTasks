# Overall project views, apps have their own views.py file.

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
   
    return redirect('accounts/home')
    #return render(request, 'index.html', context)
   
