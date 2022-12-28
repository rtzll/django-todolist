from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from accounts.forms import LoginForm, RegistrationForm
from lists.forms import TodoForm

CONST_INDEX = "lists:index"
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=request.POST["username"], password=request.POST["password"]
            )
            if user is not None and user.is_active:
                login(request, user)
                return redirect(CONST_INDEX)
        else:
            return render(request, "accounts/login.html", {"form": form})
    else:
        return render(request, "accounts/login.html", {"form": LoginForm()})

    return redirect(CONST_INDEX)


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=request.POST["username"],
                email=request.POST["email"],
                password=request.POST["password"],
            )
            return redirect("auth:login")
        else:
            return render(request, "accounts/register.html", {"form": form})
    else:
        return render(request, "accounts/register.html", {"form": RegistrationForm()})


def logout_view(request):
    logout(request)
    return redirect(CONST_INDEX)
