from django.contrib import admin
from .models import Product, Review, BookGenre


class ReviewInline(admin.TabularInline):
    model = Review


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ("title", "author", "price",)


admin.site.register(Product, ProductAdmin)
admin.site.register(BookGenre)
