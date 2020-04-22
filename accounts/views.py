from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import RegisterForm
from .models import User

# Create your views here.

# test view
def test_view(request):
    context = {
        "message" : "welcome",
    }
    return render(request, "accounts/test_template.html", context)


@csrf_exempt
def register(request):
    """Route to handle registration

    If the client uses a GET request, display the HTML page for registration
    that includes the registration form.

    If the client uses a POST request, validate the data, create a User, and
    redirect to the home page.
    """
    # TODO: remove "@csrf_exempt" after figuring out what it does
    if request.method == 'GET':
        form = RegisterForm()
        context = {'form': form}
        return render(request, "accounts/register.html", context)

    elif request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = User()
            user.username = request.POST['username']
            user.password = request.POST['password']
            user.email = request.POST['email']
            user.save()
            # Sets the username value in the session cookie
            request.session['username'] = request.POST['username']
            return HttpResponseRedirect('/')

        # TODO: Render "accounts/register.html" but send a message
        # of what error the validation caught
        context = {'form': form, 'error': 'TODO: add error here and render on front-end'}
        return render(request, "accounts/register.html", context)

    else:
        # Return HTTP 405 Method Not Allowed
        return HttpResponseNotAllowed(['POST', 'GET'])
