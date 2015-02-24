from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from lists.models import TodoList
from lists.forms import TodoForm, TodoListForm


def index(request):
    return render(request, 'lists/index.html', {'form': TodoForm()})


def todolist(request, todolist_id):
    todolist = get_object_or_404(TodoList, todolist_id)
    return render(request, 'lists/todolist.html', {'todolist': todolist})


def new_todolist(request):
    form = TodoListForm()
    user = request.user.username if request.user.is_authenticated() else None
    # ...
    return render(request, 'lists/index.html', {'form': TodoForm()})
