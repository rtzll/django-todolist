from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets

from api.serializers import UserSerializer, TodolistSerializer
from lists.models import TodoList


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class JSONResponse(HttpResponse):
    """An HttpResponse that renders its content into JSON."""
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def todolists(request):
    """List all todolists, or create a new todolist."""
    if request.method == 'GET':
        todolists = TodoList.objects.all()
        serializer = TodolistSerializer(todolists, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TodolistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def todolist_detail(request, pk):
    """Retrieve, update or delete a todolist."""
    try:
        todolist = TodoList.objects.get(pk=pk)
    except todolist.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TodoListSerializer(todolist)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TodoListSerializer(todolist, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        todolist.delete()
        return HttpResponse(status=204)