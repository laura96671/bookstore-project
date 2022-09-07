from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name="product_list"),
    path("<uuid:pk>", views.ProductDetailView.as_view(), name="product_detail"),
    path('new_product_form/', views.ProductCreate.as_view(), name="new_product_form"),

    path('edit_product/<str:pk>', views.ProductUpdate.as_view(), name="edit_product"),
    path('delete_product/<str:pk>', views.ProductDelete.as_view(), name="delete_product"),
]
