from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("/about", views.about, name="about"),
    path("/inspiring_message", views.inspiring_message, name="inspiring_message"),
    path("/math_square/<int:num>", views.math_square, name="math_square")
]