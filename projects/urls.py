from django.urls import path
from django.contrib.auth import views as auth_views  # django built-in views
from . import views # SuperTasks custom views

urlpatterns = [
    path("projects/", views.project_view, name="projects"),
    path("projects/new", views.new_project_view, name="projects_new"), 
    path('projects/<int:project_id>', views.detail_project_view, name="projects_detail"),
    path("projects/<int:project_id>/new_feature", views.new_feature_view, name="features_new"),
    #path("projects/edit_feature/<int:feature_id>", views.done2_view, name="edit_feature"),
    #temporary url below for displaying user story result will rename them to more descriptive names later.
    path("projects/done/<int:project_id>", views.done_view, name="done"), 
    path("projects/done2/<int:project_id>", views.done2_view, name="done2"),
]
 