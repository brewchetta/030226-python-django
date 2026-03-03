from django.shortcuts import render

video_list = [
    "44UGXFu-cQI?si=nbOTHgqxI0ydnixZ",
    "nGIg40xs9e4?si=bJE-BzV-GfP4t13o",
    "DLzxrzFCyOs?si=CUPc1I2BZaD5n4vp"
]


# HOME #
def home(request):
    context = {
        "videos_list": video_list
    }
    return render(request, "video_app/home.html", context)


# ABOUT #
def about(request):
    return render(request, "video_app/about.html")