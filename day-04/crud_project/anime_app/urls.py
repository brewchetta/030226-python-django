from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('animes/<int:id>/edit', views.edit_anime, name="edit_anime"),
    path('animes/<int:id>/delete', views.delete_anime, name="delete_anime"),
    path('games', views.games, name="games"),
    path('create-game', views.create_game, name="create_game"),
    path('games/<int:id>/edit', views.edit_game, name="edit_game"),
    path('games/<int:id>/delete', views.delete_game, name="delete_game"),
]
