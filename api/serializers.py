from django.contrib.auth.models import User
from rest_framework import serializers

from lists.models import TodoList


class UserSerializer(serializers.ModelSerializer):

    # todolists = serializers.HyperlinkedRelatedField(
    #     many=True, view_name='todolist-list', read_only=True)
    class Meta:
        model = User
        fields = ('url', 'username', 'last_login', 'date_joined',
                  'email')  #, 'todolists')


class TodoListSerializer(serializers.ModelSerializer):

    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = TodoList
        fields = ('id', 'title', 'created_at', 'creator', 'todos')
