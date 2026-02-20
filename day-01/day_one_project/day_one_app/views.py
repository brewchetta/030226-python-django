from django.shortcuts import render


# HOME VIEW #
def home(request):
    return render(request, "day_one_app/home.html")


# ABOUT VIEW #
def about(request):
    return render(request, "day_one_app/about.html")


# INSPIRING MESSAGE VIEW #
def inspiring_message(request):
    context = {
        "message": "You can do this!"
    }
    return render(request, "day_one_app/inspiring_message.html", context)


# MATH SQUARE VIEW #
def math_square(request, num):
    context = {
        "num": num,
        "num_squared": num ** 2,
        "example_numbers": [1,2,3,4,5,6,7,8,9,10]
    }
    return render(request, "day_one_app/math_square.html", context)