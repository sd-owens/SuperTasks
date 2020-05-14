from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("teams/", views.team_view, name="team"),

    # Future Create new Teams Route.
    #path("team/new", views.new_team_view, name="team_new"),

]
