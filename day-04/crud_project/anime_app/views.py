from django.shortcuts import render
from .models import Anime
from .forms import AnimeForm

# HOME #
def home(request):
    # if we have a post request
    if request.method == "POST":
        # fill a new version of the form with the POST data
        form = AnimeForm(request.POST)
        # checks if the form is valid and then adds it to db
        if form.is_valid():
            new_anime = Anime(
                name=form.cleaned_data["name"], 
                main_character=form.cleaned_data["main_character"],
                num_seasons=form.cleaned_data["num_seasons"]
            )
            new_anime.save()
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
