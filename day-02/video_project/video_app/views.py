from django.shortcuts import render

# HOME #
def home(request):
    return render(request, "video_app/home.html")

# ABOUT #
def about(request):
    return render(request, "video_app/about.html")