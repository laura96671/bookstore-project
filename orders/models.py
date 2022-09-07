from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product


class CartItem(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"

    def get_total_product_price(self):
        return self.quantity * self.product.price


class Cart(models.Model):
    cart_total_cost = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, unique=True)
    active = models.BooleanField(default=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)
