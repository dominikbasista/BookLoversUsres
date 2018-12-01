from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["email", "name", "place_of_live", "education", "gender",
                  "about_be", "age", "favorite_categories", "favorite_writers"]
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    # name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ["password1"]
        # fields = ["email", "password1", "password2"]


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Your password here", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat your password", widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ["name", "email","password", "password2"]

        # fields = ["email", "name", "password", "password2"]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError(message="Passwords don't match")
        return cd["password2"]