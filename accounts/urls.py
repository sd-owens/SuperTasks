from django.urls import path
from django.contrib.auth import views as auth_views  # django built-in views

from . import views # SuperTasks custom views

urlpatterns = [
    path("test/", views.test_view, name="test"),
    path("register/", views.register_view, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
