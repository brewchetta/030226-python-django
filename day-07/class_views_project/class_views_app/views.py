from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
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