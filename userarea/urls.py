from django.urls import path
from . import views


urlpatterns = [
    path("<str:pk>", views.user_favs_area, name="add_to_favs"),
    path("", views.user_favs_view, name="wishlist"),

    path("/confirm_delete/<str:pk>", views.DeleteFavs.as_view(), name="delete_fav"),
]
