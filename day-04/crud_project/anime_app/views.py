from django.shortcuts import render, get_object_or_404, redirect
from .models import Anime, AnimeGame
from .forms import AnimeForm, AnimeGameForm

# HOME #
def home(request):
    # if we have a post request
    if request.method == "POST":
        # fill a new version of the form with the POST data
        form = AnimeForm(request.POST)
        # checks if the form is valid and then adds it to db
        if form.is_valid():
            form.save()
        # if not valid show an error message
        else:
            context = {
                "form": form,
                "error": "Unable to create the new anime, please make sure you put in good information"
            }
            return render(request, "anime_app/home.html", context)

    # if we have any other type of request do this:

    # make a new instance of the form --> get a new copy of the cleaned out form to use in the html
    form = AnimeForm()
    all_anime = Anime.objects.all()
    # add the form to context so the html knows it exists
    context = { 
        "all_anime": all_anime,
        "form": form
    }
    return render(request, "anime_app/home.html", context)


# HOME (OLD) #
# def home(request):
#     # handle post requests when they happen (when the form submits)
#     if request.POST:
#         # get the data out of the POST request
#         data = request.POST.dict()
#         # build and save our anime
#         new_anime = Anime(
#             name = data["name"], 
#             main_character = data["main_character"],
#             num_seasons = data["num_seasons"]
#         )
#         new_anime.save()

#     # normal render stuff
#     all_anime = Anime.objects.all()
#     context = { "all_anime": all_anime }
#     return render(request, "anime_app/home.html", context)


# EDIT ANIME #
def edit_anime(request, id):
    anime_instance = get_object_or_404(Anime, pk=id)
    # if the form is submitted
    if request.method == "POST":
        form = AnimeForm(request.POST, instance=anime_instance)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = { 
                "anime": anime_instance,
                "form": form
            }
            return render(request, "anime_app/edit_anime.html", context)
    # render the form the first time
    form = AnimeForm(instance=anime_instance)
    context = { 
        "anime": anime_instance,
        "form": form 
    }
    return render(request, "anime_app/edit_anime.html", context)


# DELETE ANIME #
def delete_anime(request, id):
    anime_instance = get_object_or_404(Anime, pk=id)
    # if the form gets submitted delete and go home
    if request.method == "POST":
        anime_instance.delete()
        return redirect('home')

    context = { "anime": anime_instance }
    return render(request, "anime_app/delete_anime.html", context)



# GAMES INDEX #
def games(request):
    context = { 'anime_games': AnimeGame.objects.all() }
    return render(request, "anime_app/games.html", context)

# CREATE GAME #
def create_game(request):
    if request.method == "POST":
        form = AnimeGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('games')
        else:
            context = { "form": form }
            return render(request, "anime_app/create_game.html", context)

    form = AnimeGameForm()
    context = { "form": form }
    return render(request, "anime_app/create_game.html", context)


# EDIT GAME #
def edit_game(request, id):
    game_instance = get_object_or_404(AnimeGame, pk=id)

    if request.method == "POST":
        form = AnimeGameForm(request.POST, instance=game_instance)
        if form.is_valid():
            form.save()
            return redirect('games')
        else:
            context = { "form": form, "game": game_instance }
            return render(request, "anime_app/edit_game.html", context)
            
    form = AnimeGameForm(instance=game_instance)
    context = { "form": form, "game": game_instance }
    return render(request, "anime_app/edit_game.html", context)


# DELETE GAME #
def delete_game(request, id):
    game_instance = get_object_or_404(AnimeGame, pk=id)

    if request.method == "POST":
        game_instance.delete()
        return redirect('games')

    context = { "game": game_instance }
    return render(request, "anime_app/delete_game.html", context)