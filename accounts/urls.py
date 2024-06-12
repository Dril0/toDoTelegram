from django.contrib.auth import views  # importamos las views de auth app por defecto
from django.urls import path
from .views import SignupPageView

"""django.contrib.auth.urls.py en github nos provee las urls predeterminadas de auth app"""


urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
]
