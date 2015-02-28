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
        form = TodoListForm(title=request.POST['title'])
        if form.is_valid():
            todolist = TodoList(title=request.POST['title'])
            return redirect('add_todolist', todolist)
    return render(request, 'lists/overview.html', {'form': TodoListForm()})


def new_todolist(request):

    user = request.user if request.user.is_authenticated() else None

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            # create default todolist
            todolist = TodoList(creator=user)
            todolist.save()
            todo = Todo(description=request.POST['description'],
                        todolist_id=todolist.id, creator=user)
            todo.save()
            return redirect('todolist', todolist_id=todolist.id)
        # else: show error message

    return render(request, 'lists/index.html', {'form': TodoForm()})


def add_todolist(request):

    user = request.user if request.user.is_authenticated() else None

    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            todolist = TodoList(title=request.POST['title'], creator=user)
            todolist.save()
            return redirect('todolist', todolist_id=todolist.id)
        # else: show error message

    return render(request, 'lists/index.html', {'form': TodoForm()})
