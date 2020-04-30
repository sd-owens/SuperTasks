from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import login

#from .forms import RegisterForm

# Create your views here.
# test view
def project_view(request):
    context = {
        "message" : "welcome",
    }
    return render(request, "projects/test_template.html", context)
