from django.urls import path
from . import views


urlpatterns = [
    path("<str:pk>", views.user_favs_area, name="add_to_favs"),
    path("", views.user_favs_view, name="wishlist"),
    path("/confirm_delete/<str:pk>", views.DeleteFavs.as_view(), name="delete_fav"),

    path("/my_area", views.PersonalAreaView.as_view(), name="personal_area"),
    path("/reset_password", views.PasswordResetView.as_view(), name="reset_password"),
    path("/edit_inf/<str:pk>", views.PersonalAreaEdit.as_view(), name="edit_personal_info")
]
