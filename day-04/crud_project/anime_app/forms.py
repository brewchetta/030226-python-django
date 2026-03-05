from django import forms

class AnimeForm(forms.Form):
    name = forms.CharField(max_length=300)
    main_character = forms.CharField(max_length=300)
    num_seasons = forms.IntegerField()