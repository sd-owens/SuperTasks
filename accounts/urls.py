from django.urls import path
from . import views #import all account views

urlpatterns = [
    path("test/", views.test_view, name="test"),
    path("register/", views.register, name="register")
]
