from django.contrib.auth import views  # importamos las views de auth app por defecto
from django.urls import path

"""django.contrib.auth.urls.py en github nos provee las urls predeterminadas de auth app"""


urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path(
        "password_change/", views.PasswordChangeView.as_view(), name="password_change"
    ),
    path(
        "password_change/done/",
        views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reser/done/",
        views.PasswordChangeDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token</",
        views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
