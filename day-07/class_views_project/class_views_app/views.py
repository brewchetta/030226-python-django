from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, FormView
from .forms import WeatherForm
from .models import Weather


# HOME (OLD) #
# def home(request):
#     return render(request, "class_views_app/home.html")


# HOME #
class HomeView(TemplateView):
    template_name = "class_views_app/home.html"


# ABOUT #
class AboutView(TemplateView):
    template_name = "class_views_app/about.html"


# MORNING MESSAGE (OLD) #
# def morning_message(request):
#     message = "Good morning and welcome to Django"
#     context = { "message": message }
    
#     return render(request, "class_views_app/morning_message.html", context)


# MORNING MESSAGE #
class MorningMessageView(TemplateView):
    # template name is for the html that will be rendered
    template_name = "class_views_app/morning_message.html"
    # extra context is the same as context in a functional component
    extra_context = { 
        "message": "Good morning and welcome to Django",
        "todays_breakfast": "Cheese & Grits"
    }


# WEATHER FORM (OLD) #
# def weather_form(request):
#     # POST #
#     if request.method == "POST":
#         form = WeatherForm(request.POST)
#         if form.is_valid():
#             form.save()
#             context = { "form": WeatherForm(), "weather": Weather.objects.all() }
#             return render(request, "class_views_app/weather_form.html", context)
#         else:
#             context = { 
#                 "form": form,
#                 "weather": Weather.objects.all()
#             }
#             return render(request, "class_views_app/weather_form.html", context)

#     # SHOW THE PAGE
#     form = WeatherForm()
#     weather = Weather.objects.all()
#     context = { 
#         "form": form, 
#         "weather": weather
#     }
#     return render(request, "class_views_app/weather_form.html", context)


# WEATHER #
class WeatherView(View):
    template_name = "class_views_app/weather_form.html"
    form_class = WeatherForm

    # SHOW THE PAGE / GET REQUEST
    def get(self, request):
        form = self.form_class()
        weather = Weather.objects.all()

        context = {
            "form": form,
            "weather": weather
        }

        return render(request, self.template_name, context)
    
    # SUBMIT THE FORM / POST REQUEST
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            context = { "form": self.form_class(), "weather": Weather.objects.all() }
            return render(request, "class_views_app/weather_form.html", context)
        else:
            context = { 
                "form": form,
                "weather": Weather.objects.all()
            }
            return render(request, self.template_name, context)
        

# WEATHER FORM #
class WeatherFormView(FormView):
    # template is the html to show
    template_name = "class_views_app/weather_form.html"
    # form is the form to show/use
    form_class = WeatherForm
    # when we've successfully completed the form, send us to this page
    success_url = "/weather"
    # this will trigger and save the form to the db when it's validated
    def form_valid(self, form):
        form.save()
        return super().form_valid( form )
    

from django.views.generic import ListView
# WEATHER LIST VIEW #
class WeatherListView(ListView):
    model = Weather
    context_object_name = "weather_reports"
    queryset = Weather.objects.order_by("city")


from django.views.generic import DetailView
# WEATHER DETAIL VIEW #
class WeatherDetailView(DetailView):
    model = Weather
    context_object_name = "weather"



# USING AN API IN A VIEW
import requests
from django.conf import settings

# look at settings.py to find out how the api key is retrieved
API_KEY = settings.WEATHER_API_KEY

def get_weather(request, city):
    # get json from api by plugging in api key and city
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no")
    # parse response
    data = response.json()

    weather_data = {
    "city": data["location"]["name"],
    "region": data["location"]["region"],
    "country": data["location"]["country"],
    "temp_f": data["current"]["temp_f"],
    "condition": data["current"]["condition"]["text"],
    "wind_mph": data["current"]["wind_mph"],
    "humidity": data["current"]["humidity"]
    }

    context = { "weather_data": weather_data }
    # render page
    return render(request, "class_views_app/get_weather.html", context)

# RETURN AT 3:33 EST
# RETURN AT 3:33 EST
# RETURN AT 3:33 EST
# RETURN AT 3:33 EST
# RETURN AT 3:33 EST
# RETURN AT 3:33 EST