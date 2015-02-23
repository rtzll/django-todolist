from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from lists.models import TodoList


def index(request):
    return HttpResponse('Hello, world.')


def todolist(request, todolist_id):
    todolist = get_object_or_404(TodoList, todolist_id)
    return render(request, 'lists/todolist.html', {'todolist': todolist})
