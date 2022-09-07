from products.models import Product
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class UserFavs(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    added = models.BooleanField(default=False)

    def __str__(self):
        return str(self.products)

    def get_delete_from_favs(self):
        return reverse("delete_fav", kwargs={"pk": str(self.pk)})


class UserArea(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user)
