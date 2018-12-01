from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from .models import UserProfile
from .forms import UserProfileForm, UserRegisterForm, UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, "home.html", {})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            messages.success(request, f'Account created for {username}. Now you can login' )
            return redirect("login")
        else:
            print("dupa!!!")
    else:
        form = UserCreationForm()

    return render(request, "register.html", {'form': form})


def register_1(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, f'Account created for {name}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def register_2(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, "register_done.html",{'new_user': new_user})
    else:
            form = UserRegistrationForm()
    return render(request, "register.html", {"form": form})


def login_1():
    pass

@login_required
def user(request, user_id):
    user = get_object_or_404(UserProfile, id=user_id)
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
    else:
        form = UserProfileForm()
    return render(request, 'user_profile.html', {'user': user, 'form': form})


@login_required
def profile(request):
    return render(request, "profile.html" )


class UserView(TemplateView):
    template = "/user_profile.html"

    def get(self, request):
        form = UserProfileForm()
