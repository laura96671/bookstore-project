from django.test import TestCase, Client
from django.urls import reverse

from .models import Product


class ProductTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(title="Harry Potter",
                                              author="JK Rowling",
                                              price="25.00",)

    def test_product_listing(self):
        self.assertEqual(f'{self.product.title}', "Harry Potter")
        self.assertEqual(f'{self.product.author}', "JK Rowling")
        self.assertEqual(f'{self.product.price}', "25.00")

    def test_product_list_view(self):
        response = self.client.get(reverse("product_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_list.html")
        self.assertContains(response, "Harry Potter")

    def test_product_detail_view(self):
        response = self.client.get(self.product.get_absolute_url())
        no_response = self.client.get("/products/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, "products/product_detail.html")
        self.assertContains(response, "Harry Potter")

    def test_new_product_creation_view(self):
        response = self.client.get(reverse("new_product_form"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/new_product_form.html")
        self.assertContains(response, "New Product")
