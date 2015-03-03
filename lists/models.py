from django.db import models
from django.contrib.auth.models import User


class TodoList(models.Model):
    title = models.CharField(max_length=128, default='untitled')
    created_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, null=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.title

    def count(self):
        return self.todo_set.count()

    def count_finished(self):
        return self.todo_set.filter(is_finished=True).count()

    def count_open(self):
        return self.todo_set.filter(is_finished=False).count()


class Todo(models.Model):
    description = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now=True)
    finished_at = models.DateTimeField(null=True)
    is_finished = models.BooleanField(default=False)
    creator = models.ForeignKey(User, null=True)
    todolist = models.ForeignKey(TodoList)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.description
