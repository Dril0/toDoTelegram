"""
URL configuration for toDoTelegram project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "accounts/", include("django.contrib.auth.urls")
    ),  # incluimos las urls por defecto de auth app --> login, logout, passwords and resets. con el template context de django nos permite cargar los templates con data correspondiente a las views. usamos user tags para acceder a los atributos, por ejemplo user.email.
    path("accounts/", include("accounts.urls")),
    path("todo/", include("toDo.urls")),
    path("", include("pages.urls")),
]
