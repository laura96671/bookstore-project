from django.urls import path
from .views import home_view, AboutPage

urlpatterns = [
    path('', home_view, name="home"),
    path('about/', AboutPage.as_view(), name="about"),
]
