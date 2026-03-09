from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()

# UserCreationForm is a special ModelForm just for the User
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# Form is the most generic type of forms so we need to define every field
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


# ModelForm is a form that automatically figures out the fields / inputs
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["age", "bio", "location"]