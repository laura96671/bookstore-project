import stripe
from products.models import Product
from .models import Cart, CartItem
from django.views.generic import TemplateView
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect
from datetime import timezone
from .forms import CartForm
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic.detail import SingleObjectMixin


stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


class OrdersView(TemplateView):
    template_name = "orders/purchase.html"

    def get_context_data(self, **kwargs):
        product = Product.objects.get(id=self.kwargs["pk"])
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        context["product"] = product
        return context


def charge(request):
    permission = Permission.objects.get(codename="special_status")
    u = request.user
    u.user_permissions.add(permission)

    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=3900,
            currency='usd',
            description='Purchase all books',
            source=request.POST['stripeToken']
        )
        return render(request, 'orders/charge.html')


@login_required
def add_to_cart_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order_item, created = CartItem.objects.get_or_create(product=product, user=request.user, ordered=False)

    if not created:
        order_item.quantity += 1
        order_item.save()
        messages.info(request, "This item quantity was updated.")

    order_qs = Cart.objects.filter(user=request.user, ordered=False)

    if not order_qs.exists():
        order = Cart.objects.create(user=request.user, cart_total_cost=product.price)
        order.save()
        messages.info(request, "This item was added to your cart.")

    else:
        current_order = order_qs.first()
        current_order.cart_total_cost += product.price
        current_order.save()

    return redirect("/")


def cart_view(request):
    order_item = CartItem.objects.filter(user=request.user)
    context = {"order_item": order_item}

    return render(request, "orders/cart.html", context)



