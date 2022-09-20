import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class BookAge(models.Model):
    book_age = models.CharField(max_length=250)

    def __str__(self):
        return self.book_age


class BookMood(models.Model):
    book_mood = models.CharField(max_length=50)

    def __str__(self):
        return self.book_mood


class BookGenre(models.Model):
    book_genre = models.CharField(max_length=50)

    def __str__(self):
        return self.book_genre


'''
def get_default_book_genre():
    genre, created = BookGenre.objects.get_or_create(book_genre="unknown")
    return genre.pk
'''


class Product(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    number_of_pages = models.IntegerField(default=0, blank=True)
    book_genre = models.ForeignKey(BookGenre, on_delete=models.DO_NOTHING)
    book_age = models.ForeignKey(BookAge, on_delete=models.DO_NOTHING, blank=True, null=True)
    book_mood = models.ForeignKey(BookMood, on_delete=models.DO_NOTHING, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    book_image = models.ImageField(upload_to="covers/", blank=True)

    class Meta:
        permissions = [
            ("special_status", "Can read all books"),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={'pk': str(self.pk)})

    def get_add_to_cart_url(self):
        return reverse("add_to_cart", kwargs={'pk': str(self.pk)})

    def get_add_to_favs_url(self):
        return reverse("add_to_favs", kwargs={"pk": str(self.pk)})


class Review(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name="reviews",)
    review = models.CharField(max_length=250)
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.CASCADE,)

    def __str__(self):
        return self.review
