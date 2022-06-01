from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import ProductsPage

class ProductsPageTest(SimpleTestCase):

    def setUp(self):
        url = reverse("products")
        self.response = self.client.get(url)

    def test_products_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_products_template_used(self):
        self.assertTemplateUsed(self.response, "products.html")

    def test_products_contains_correct_html(self):
        self.assertContains(self.response, "Products")

    def test_products_not_contains_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there, I should not be on the page.")

    def test_products_url_resolves_productspage(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, ProductsPage.as_view().__name__)
