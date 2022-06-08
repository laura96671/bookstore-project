from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Product
from django.http import HttpResponseRedirect
from .forms import NewProductForm


class ProductListView(ListView):
    model = Product
    context_object_name = "product_list"
    template_name = "products/product_list.html"


class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    template_name = "products/product_detail.html"

def new_product_form(request):
    form = NewProductForm(request.POST or None, request.FILES or None)
    context = {}

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/products')

    context['form'] = form
    return render(request, "products/new_product_form.html", context)
