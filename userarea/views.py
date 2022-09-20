from django.shortcuts import render, redirect
from products.models import Product
from users.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DeleteView, CreateView, UpdateView
from .models import UserFavs, UserArea
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from products.views import ProductDelete


@login_required
def user_favs_area(request, pk):
    product = get_object_or_404(Product, pk=pk)
    UserFavs.objects.get_or_create(user=request.user, products=product, added=False)

    return redirect("/")


def user_favs_view(request):
    fav_item = UserFavs.objects.filter(user=request.user)
    context = {"favourite_item": fav_item}

    return render(request, "personal_area/favourite_books.html", context)


class DeleteFavs(LoginRequiredMixin, DeleteView):
    model = UserFavs
    template_name = "personal_area/favourite_confirm_delete.html"
    success_url = reverse_lazy("wishlist")


'''
def delete_from_fav(request, pk):
    userfavs = get_object_or_404(UserFavs, pk=pk)

    if request.method == "GET":
        context = {"userfavs": userfavs}
        return render(request, "personal_area/favourite_confirm_delete.html", context)

    userfavs.delete()
    fav_item = UserFavs.objects.filter(user=request.user)
    context = {"favourite_item": fav_item}
    return render(request, "personal_area/favourite_books.html", context)
'''


class PersonalAreaView(CreateView):
    model = CustomUser
    fields = '__all__'
    template_name = "personal_area/personal_area.html"


class PersonalAreaEdit(UpdateView):
    model = CustomUser
    fields = ["username", "email", "your_description"]
    template_name = "personal_area/personal_area_update_info.html"
    success_url = reverse_lazy("personal_area")


class PasswordResetView(PasswordChangeView):
    success_url = reverse_lazy("personal_area")
    template_name = "personal_area/password_reset/reset_password_form.html"
