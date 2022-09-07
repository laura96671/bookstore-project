from django.urls import path
from . import views


urlpatterns = [
    path("<str:pk>", views.add_to_cart_view, name="add_to_cart"),
    path("", views.cart_view, name="cart")
]
