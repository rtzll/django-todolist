from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from lists.models import TodoList
from lists.forms import TodoForm, TodoListForm


def index(request):
    return render(request, 'lists/index.html', {'form': TodoForm()})


def todolist(request, todolist_id):
    todolist = get_object_or_404(TodoList, todolist_id)
    return render(request, 'lists/todolist.html',
                  {'todolist': todolist, 'form': TodoForm()})


@login_required
def overview(request):
    if request.method == 'POST':
        todolist = None
        # ...
        return redirect('add_todolist', todolist)
    return render(request, 'lists/overview.html', {'form': TodoListForm()})


def new_todolist(request):
    if request.method == 'POST':
        form = TodoListForm()
        user = request.user.username if request.user.is_authenticated() else None
        # ...
        return redirect('todolist', todolist_id=1)

    return render(request, 'lists/index.html', {'form': TodoForm()})


def add_todolist(request):
    if request.method == 'POST':
        form = TodoListForm()
        user = request.user.username if request.user.is_authenticated() else None
        # ...
        return redirect('todolist', todolist_id=1)

    return render(request, 'lists/index.html', {'form': TodoForm()})
