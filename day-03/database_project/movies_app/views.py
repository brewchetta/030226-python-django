from django.shortcuts import render, get_object_or_404
from .models import Movie

# HOME (OLD VERSION) #
# def home(request):
#     # get all movies from the db
#     all_movies = Movie.objects.all()
#     # put the movies into context
#     context = { "all_movies": all_movies }
#     # render page with context
#     return render(request, "movies_app/home.html", context)

# HOME #
def home(request):
    movies_query_set = Movie.objects

    # get movies for 2026
    # movies_query_set = movies_query_set.filter( release_year=2026 )

    # gets movies before 2026
    # movies_query_set = movies_query_set.filter( release_year__lt=2026 )

    # gets movies with the word `predator` in their title
    # movies_query_set = movies_query_set.filter( title__icontains="predator" )

    # http://127.0.0.1:8000/?title=predator&release_year=2026
    # title=predator
    query_title = request.GET.get('title')
    # release_year=2026
    query_release_year = request.GET.get('release_year')
    
    # if you have the query_title then filter
    if query_title:
        movies_query_set = movies_query_set.filter(title__icontains=query_title)
    # if you have the query_release_year then filter
    if query_release_year:
        movies_query_set = movies_query_set.filter(release_year=query_release_year)

    context = { "all_movies": movies_query_set.all() }

    return render(request, "movies_app/home.html", context)

# MOVIE DETAIL #
def movie_detail(request, id):
    # go find the movie with a `primary key` of the passed in `id`
    movie = get_object_or_404(Movie, pk=id)
    context = { "movie": movie }
    return render(request, "movies_app/movie_detail.html", context)