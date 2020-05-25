from django.urls import path

from . import views

urlpatterns = [
    #path("", views.dashboard_view, name="dashboard"),
    path("", views.team_view, name="team_view"),

    path("new/", views.new_team_view, name="new_team"),

    path("<int:team_id>", views.team_view, name="team"),

]
