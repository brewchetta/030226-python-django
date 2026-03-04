from django.shortcuts import render, get_object_or_404
from .models import Movie

# HOME #
def home(request):
    # get all movies from the db
    all_movies = Movie.objects.all()
    # put the movies into context
    context = { "all_movies": all_movies }
    # render page with context
    return render(request, "movies_app/home.html", context)

# MOVIE DETAIL #
def movie_detail(request, id):
    # go find the movie with a `primary key` of the passed in `id`
    movie = get_object_or_404(Movie, pk=id)
    context = { "movie": movie }
    return render(request, "movies_app/movie_detail.html", context)