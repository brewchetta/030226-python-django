from django.contrib import admin
from .models import Movie, MovieCharacter, Genre

admin.site.register(Movie)
admin.site.register(MovieCharacter)
admin.site.register(Genre)