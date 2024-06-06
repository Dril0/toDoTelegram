from django.contrib.auth import (
    get_user_model,
)  # mira directamente en AUTH_USER_MODEL en settings.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:  # define datos y configuraciones adicionales, el modelo asocioado al formulario y los campos a inclur. Password esta implicitamente incluido.
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )
