from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),

    path('about', views.AboutView.as_view(), name="about"),

    path('morning-message', views.MorningMessageView.as_view(), name="morning_message"),

    path('weather', views.WeatherView.as_view(), name="weather"),

    path('weather-form', views.WeatherFormView.as_view(), name="weather-form"),

    path('weather-list', views.WeatherListView.as_view(), name="weather_list"),
    
    path('weather/<int:pk>', views.WeatherDetailView.as_view(), name="weather_detail"),

    path("get-weather/<slug:city>", views.get_weather, name="get_weather")
]