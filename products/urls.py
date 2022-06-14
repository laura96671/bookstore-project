from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductListView.as_view(), name="product_list"),
    path("<uuid:pk>", views.ProductDetailView.as_view(), name="product_detail"),
    path('new_product_form/', views.new_product_form, name="new_product_form"),

    path('edit_product/<str:pk>', views.product_edit, name="edit_product"),
    path('delete_product/<str:pk>', views.delete_product, name="delete_product"),
]
