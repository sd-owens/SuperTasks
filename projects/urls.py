from django.urls import path
from django.contrib.auth import views as auth_views  # django built-in views

from . import views # SuperTasks custom views

urlpatterns = [
    path("projects/", views.project_view, name="projects"),
    
    path("projects/new", views.new_project_view, name="projects_new"), 
    #TODO: add view for project with all its features
    path("projects/1", views.detail_project_view, name="projects_detail"), 
    path("projects/feature", views.feature_view, name="features"), 
    path("projects/done", views.done_view, name="done"), 
]
