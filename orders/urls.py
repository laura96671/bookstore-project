from django.urls import path
from .views import OrdersView, charge


urlpatterns = [
    path('charge', charge, name="charge"),
    path('/<str:pk>', OrdersView.as_view(), name="orders"),
]
