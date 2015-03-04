from django.contrib.auth.models import User, Group

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status

from api.serializers import UserSerializer, TodoListSerializer
from lists.models import TodoList


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET', 'POST'])
def todolists(request):
    """List all todolists, or create a new todolist."""

    if request.method == 'GET':
        todolists = TodoList.objects.all()
        serializer = TodoListSerializer(todolists, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TodoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def todolist_detail(request, pk):
    """Retrieve, update or delete a todolist."""
    try:
        todolist = TodoList.objects.get(pk=pk)
    except todolist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodoListSerializer(todolist)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TodoListSerializer(todolist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todolist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)