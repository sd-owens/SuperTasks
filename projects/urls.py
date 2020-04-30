from django.urls import path
from django.contrib.auth import views as auth_views  # django built-in views

from . import views # SuperTasks custom views

urlpatterns = [
    path("projects/", views.project_view, name="projects"),
    #toDo: add views for new project
    #path("projects/new", views.project_new_view, name="projects_new"), 
]
