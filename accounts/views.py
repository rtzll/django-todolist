from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from accounts.forms import LoginForm, RegistrationForm
from lists.forms import TodoForm


def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'lists/index.html',
                              {'form': TodoForm()})
    else:
        return render(request, 'accounts/login.html', {'form': LoginForm()})

    return render(request, 'lists/index.html', {'form': TodoForm()})

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        # TODO add proper password check
        assert password == password_confirmation
        User.objects.create_user(username, email=email, password=password)
    else:
        return render(request, 'accounts/register.html',
                      {'form': RegistrationForm()})


def logout_view(request):
    logout(request)
