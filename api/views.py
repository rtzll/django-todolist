from django.contrib.auth.models import User
from django.http import Http404

from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets

from api.serializers import UserSerializer, TodoListSerializer
from lists.models import TodoList


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TodoLists(generics.ListCreateAPIView):

    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class TodoListDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
