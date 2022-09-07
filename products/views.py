from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Product
from django.http import HttpResponseRedirect


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = "product_list"
    template_name = "products/product_list.html"
    login_url = "account_login"


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = "product"
    template_name = "products/product_detail.html"
    login_url = "account_login"


class ProductCreate(PermissionRequiredMixin, CreateView):
    permission_required = "products.can_add_product"
    model = Product
    fields = "__all__"
    success_url = reverse_lazy("product_list")


class ProductUpdate(UpdateView):
    model = Product
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy("product_detail", kwargs={'pk': self.object.pk})


class ProductDelete(PermissionRequiredMixin, DeleteView):
    permission_required = "products.can_delete_product"
    model = Product
    success_url = reverse_lazy("product_list")
