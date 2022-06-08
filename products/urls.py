from django.urls import path
from .views import ProductListView, ProductDetailView, new_product_form

urlpatterns = [
    path('', ProductListView.as_view(), name="product_list"),
    path("<uuid:pk>", ProductDetailView.as_view(), name="product_detail"),
    path('new_product_form/', new_product_form, name="new_product_form"),
]
