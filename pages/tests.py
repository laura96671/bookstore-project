from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPage


class HomepageTest(SimpleTestCase):

    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_contains_correct_html(self):
        self.assertContains(self.response, "Bookstore")

    def test_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there, I should not be on the page.')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTest(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, "about.html")

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, "About")

    def test_aboutpage_not_contains_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there, I should not be on the page.')

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, AboutPage.as_view().__name__)
