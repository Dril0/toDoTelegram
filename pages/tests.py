from django.test import (
    SimpleTestCase,
)  # se usa para webpages que no tienen un modelo incluido
from django.urls import reverse

# Create your tests here.


class HomepageTests(SimpleTestCase):
    def setUp(self):
        """seteamos variable a url, para no repetir en todos los test, setUp es un metodoo de ayuda"""
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_homepage_contains_correct_html(self):
        response = self.client.get("/")
        self.assertContains(response, "Bienvenidos al Himalaya")

    def test_homepage_not_contains_incorrect_html(self):
        response = self.client.get("/")
        self.assertNotContains(response, "Esto no tendria que estar aca")
