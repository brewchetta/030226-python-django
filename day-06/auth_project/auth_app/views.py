from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, EditProfileForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# HOME #
def home(request):
    return render(request, "auth_app/home.html")


# SIGNUP #
def signup(request):
    # if someone submits the form...
    if request.method == "POST":
        # validate and create the user
        form = SignUpForm(request.POST)
        # if user submitted good data save the user
        if form.is_valid():
            user = form.save()
            # login() will make sure the user is logged in
            login(request, user)
            return redirect("home")
        # otherwise rerender the form which will show its errors
        else:
            context = { "form": form }
            return render(request, "auth_app/signup.html", context)
    
    # if any other request create and pass the form through with context
    form = SignUpForm()
    context = { "form": form }
    return render(request, "auth_app/signup.html", context)


# LOGIN #
def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # grab data that the user passed in the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # check to see if a user matches the username and password
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")
        # if something goes wrong show the form again but with a message
        context = { "form": form, "message": "Invalid username or password" }
        return render(request, "auth_app/login_user.html", context)

    form = LoginForm()
    context = { "form": form }
    return render(request, "auth_app/login_user.html", context)


# LOGOUT #
@login_required
def logout_user(request):
    logout(request)
    return redirect("home")
# logout will delete the sessionid so that a user is not logged in


# PROFILE #
@login_required
def profile(request):
    user_profile = request.user.profile
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
        context = { "form": form }
        return render(request, "auth_app/profile.html", context)

    form = EditProfileForm(instance=user_profile)
    context = { "form": form }
    return render(request, "auth_app/profile.html", context)