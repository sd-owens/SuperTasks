"""SuperTasks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views  # SuperTasks project main views.py  /SuperTasks/SuperTasks/views.py

from django.conf.urls.static import static #used for image path
from django.conf import settings #used for image path

urlpatterns = [
    # project landing page '/' route
    path('', views.index, name='index'),
    # admin page
    path('admin/', admin.site.urls),
    #include account model urls
    path("accounts/", include("accounts.urls")),
    #include projects model urls
    path('', include("projects.urls")),
    #include teams model urls
    path('teams/', include("teams.urls")),
]

#Make sure django looks for images in the static/images folder
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)