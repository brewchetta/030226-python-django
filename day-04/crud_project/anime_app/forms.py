from django import forms
from .models import Anime, AnimeGame

# without character model (generic form)
# class AnimeForm(forms.Form):
#     name = forms.CharField(max_length=300)
#     main_character = forms.CharField(max_length=300)
#     num_seasons = forms.IntegerField()

# with character model (special form for models)
class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ['name', 'main_character', 'num_seasons']


class AnimeGameForm(forms.ModelForm):
    class Meta:
        model = AnimeGame
        fields = ['name', 'anime']