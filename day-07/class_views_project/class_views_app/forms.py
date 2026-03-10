from django import forms
from .models import Weather

class WeatherForm(forms.ModelForm):
    class Meta:
        model = Weather
        fields = ['date', 'city', 'country', 'temp_f', 'condition', 'wind_speed_mph']