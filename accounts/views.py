from django.shortcuts import render

# Create your views here.

# test view
def test_view(request):
    context = {
        "message" : "welcome",
    }
    return render(request, "accounts/test_template.html", context)