from django.contrib.auth.models import User
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status

from api.serializers import UserSerializer, TodoListSerializer
from lists.models import TodoList


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""
    queryset = User.objects.all()
    serializer_class = UserSerializer



class TodoLists(APIView):
    """List all todolists, or create a new todolist."""

    def get(self, request):
        todolists = TodoList.objects.all()
        serializer = TodoListSerializer(todolists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoListDetail(APIView):
    """Retrieve, update or delete a todolist."""
    def get_object(self, pk):
        try:
            return TodoList.objects.get(pk=pk)
        except TodoList.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        todolist = self.get_object(pk)
        serializer = TodoListSerializer(todolist)
        return Response(serializer.data)

    def put(self, request, pk):
        todolist = self.get_object(pk)
        serializer = TodoListSerializer(todolist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        todolist = self.get_object(pk)
        todolist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
