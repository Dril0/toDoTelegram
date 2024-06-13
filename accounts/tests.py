from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve  # new
from .forms import CustomUserCreationForm  # new
from .views import SignupPageView  # new

# Create your tests here.


class CustomUserTests(TestCase):
    pass


class SignUpPageTests(TestCase):  # new
    """nuestro setUp carga la pagina que queremos testear."""

    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "registration/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_signup_form(self):  # new
        form = self.response.context.get(
            "form"
        )  # obtenemos el context form de la variable self.response de setUp
        self.assertIsInstance(
            form, CustomUserCreationForm
        )  # Verifica que el formulario es una instancia de CustomUserCreationForm
        self.assertContains(
            self.response, "csrfmiddlewaretoken"
        )  # verificamos que tenemosel csrf token

    def test_signup_view(self):  # new
        view = resolve(
            "/accounts/signup/"
        )  # resolve se usa en tests para verificar que una URL específica se resuelva a una vista específica
        self.assertEqual(
            view.func.__name__, SignupPageView.as_view().__name__
        )  # verificamos que retorne el mismo nombre
