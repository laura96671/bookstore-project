from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Product
from django.http import HttpResponseRedirect
from .forms import NewProductForm
from django.contrib.auth.decorators import permission_required


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = "product_list"
    template_name = "products/product_list.html"
    login_url = "account_login"


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Product
    context_object_name = "product"
    template_name = "products/product_detail.html"
    login_url = "account_login"
    permission_required = "products.special_status"


@permission_required("products.can_add_product")
def new_product_form(request):
    form = NewProductForm(request.POST or None, request.FILES or None)
    context = {}

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/products')

    context['form'] = form
    return render(request, "products/new_product_form.html", context)


def product_edit(request, pk):
    context = {}

    product = Product.objects.get(id=pk)
    form = NewProductForm(instance=product)

    if request.method == 'POST':
        form = NewProductForm(request.POST or None, request.FILES or None, instance=product)
        form.save()
        return HttpResponseRedirect('/products')

    context['form'] = form
    return render(request, "products/new_product_form.html", context)


@permission_required("products.can_delete_product")
def delete_product(request, pk):
    item = Product.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return HttpResponseRedirect('/products')

    context = {"product": item}
    return render(request, "products/delete_product.html", context)
