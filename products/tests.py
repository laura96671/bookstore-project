from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase, Client
from django.urls import reverse

from .models import Product, Review


class ProductTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username="reviewuser",
                                                         email="reviewuser@email.com",
                                                         password="testpass123",)

        self.admin_user = get_user_model().objects.create_superuser(username="superuser",
                                                                    email="superuser@email.com",
                                                                    password="testpass123")

        self.special_permission = Permission.objects.get(codename="special_status")

        self.product = Product.objects.create(title="Harry Potter",
                                              author="JK Rowling",
                                              price="25.00",)

        self.review = Review.objects.create(product=self.product,
                                            author=self.user,
                                            review="Amazing book!",)

    def test_product_listing(self):
        self.assertEqual(f'{self.product.title}', "Harry Potter")
        self.assertEqual(f'{self.product.author}', "JK Rowling")
        self.assertEqual(f'{self.product.price}', "25.00")

    def test_new_product_creation_view_for_superuser(self):
        self.client.login(email="superuser@email.com", password="testpass123")
        response = self.client.get(reverse("new_product_form"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/new_product_form.html")
        self.assertContains(response, "New Product")

    def test_product_list_view_for_logged_in_user(self):
        self.client.login(email="reviewuser@email.com", password="testpass123")
        response = self.client.get(reverse("product_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "products/product_list.html")

    def test_product_list_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse("product_list"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '%s?next=/products/' % reverse("account_login"))
        response = self.client.get('%s?next=/products/' % reverse("account_login"))
        self.assertContains(response, "Log in")

    def test_product_detail_view_with_permissions(self):
        self.client.login(email="reviewuser@email.com", password="testpass123")
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.product.get_absolute_url())
        no_response = self.client.get("/products/12345")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Harry Potter")
        self.assertContains(response, "Amazing book!")
        self.assertTemplateUsed(response, "products/product_detail.html")
