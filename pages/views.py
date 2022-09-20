from django.views.generic import TemplateView
from django.db.models import Q
from django.shortcuts import render
from products.models import Product, BookGenre, BookMood, BookAge
from userarea.models import UserFavs
import json


def home_view(request):
    template_name = "home.html"
    book_genre = BookGenre.objects.all()
    book_mood = BookMood.objects.all()
    book_age = BookAge.objects.all()
    user_favs = UserFavs.objects.all()
    context = {"book_genres": book_genre,
               "book_moods": book_mood,
               "book_ages": book_age,
               "wishlist": user_favs}

    if request.method == "POST":
        genre_check = request.POST.getlist("genre_check")
        mood_check = request.POST.getlist("mood_check")
        age_check = request.POST.getlist("age_check")

        book_showed = Product.objects.filter(Q(book_genre__book_genre__in=genre_check) |
                                             Q(book_mood__book_mood__in=mood_check) |
                                             Q(book_age__book_age__in=age_check))
        context["book_showed"] = book_showed

        return render(request, template_name, context)

    return render(request, template_name, context)


class AboutPage(TemplateView):
    template_name = "about.html"
