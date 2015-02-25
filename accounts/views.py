from django.contrib.auth import authenticate, login, logout

from lists.forms import TodoForm


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render(request, 'lists/index.html', {'form': TodoForm()})
    return render(request, 'lists/index.html', {'form': TodoForm()})

def register(request):
    pass

def logout_view(request):
    logout(request)
