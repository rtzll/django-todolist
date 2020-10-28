from django.contrib.auth.models import User
from rest_framework import serializers

from lists.models import Todo, TodoList


class UserSerializer(serializers.ModelSerializer):

    todolists = serializers.PrimaryKeyRelatedField(
        many=True, queryset=TodoList.objects.all()
    )

    class Meta:
        model = User
        fields = ("id", "username", "last_login", "date_joined", "todolists")


class TodoListSerializer(serializers.ModelSerializer):

    creator = serializers.ReadOnlyField(source="creator.username")

    class Meta:
        model = TodoList
        fields = ("id", "title", "created_at", "creator", "todos")


class TodoSerializer(serializers.ModelSerializer):

    creator = serializers.ReadOnlyField(source="creator.username")

    class Meta:
        model = Todo
        fields = (
            "id",
            "todolist",
            "description",
            "created_at",
            "creator",
            "is_finished",
            "finished_at",
        )
