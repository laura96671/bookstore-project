import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Product(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    book_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={'pk': str(self.pk)})


class Review(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name="reviews",)
    review = models.CharField(max_length=250)
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.CASCADE,)

    def __str__(self):
        return self.review
