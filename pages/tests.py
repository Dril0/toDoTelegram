from django.test import (
    SimpleTestCase,
)  # se usa para webpages que no tienen un modelo incluido
from django.urls import reverse, resolve
from .views import HomePageView

# Create your tests here.


class HomepageTests(SimpleTestCase):
    def setUp(self):
        """seteamos variable a url, para no repetir en todos los test, setUp es un metodoo de ayuda"""
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "Bienvenidos al Himalaya")

    def test_homepage_not_contains_incorrect_html(self):
        self.assertNotContains(self.response, "Esto no tendria que estar aca")

    def test_homepage_url_resolves_homepageview(self):
        """testeamos que la view haga matc con HomePageView"""
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
