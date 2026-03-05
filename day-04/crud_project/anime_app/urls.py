from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('animes/<int:id>/edit', views.edit_anime, name="edit_anime"),
    path('animes/<int:id>/delete', views.delete_anime, name="delete_anime"),
]
