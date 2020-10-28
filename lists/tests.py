from unittest import skip

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from lists.forms import TodoForm, TodoListForm
from lists.models import Todo, TodoList


class ListTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("test", "test@example.com", "test")
        self.todolist = TodoList(title="test title", creator=self.user)
        self.todolist.save()
        self.todo = Todo(
            description="save todo", todolist_id=self.todolist.id, creator=self.user
        )
        self.todo.save()
        self.client.login(username="test", password="test")

    def tearDown(self):
        self.client.logout()
        self.user.delete()
        self.todolist.delete()
        self.todo.delete()

    def test_get_index_page(self):
        response = self.client.get(reverse("lists:index"))
        self.assertTemplateUsed(response, "lists/index.html")
        self.assertIsInstance(response.context["form"], TodoForm)

    def test_add_todo_to_index_page(self):
        response = self.client.post(reverse("lists:index"), {"description": "test"})
        self.assertTemplateUsed(response, "lists/index.html")
        self.assertIsInstance(response.context["form"], TodoForm)

    def test_get_todolist_view(self):
        response = self.client.get(
            reverse("lists:todolist", kwargs={"todolist_id": self.todolist.id})
        )
        self.assertTemplateUsed(response, "lists/todolist.html")
        self.assertIsInstance(response.context["form"], TodoForm)

    def test_add_todo_to_todolist_view(self):
        response = self.client.post(
            reverse("lists:todolist", kwargs={"todolist_id": self.todolist.id}),
            {"description": "test"},
        )
        self.assertTemplateUsed(response, "lists/todolist.html")
        self.assertIsInstance(response.context["form"], TodoForm)
        self.assertContains(response, "test")

    def test_get_todolist_overview(self):
        response = self.client.get(reverse("lists:overview"))
        self.assertTemplateUsed(response, "lists/overview.html")
        self.assertIsInstance(response.context["form"], TodoListForm)

    def test_get_todolist_overview_redirect_when_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse("lists:overview"))
        self.assertRedirects(response, "/auth/login/?next=/todolists/")

    def test_add_todolist_to_todolist_overview(self):
        response = self.client.post(reverse("lists:overview"), {"title": "some title"})
        self.assertRedirects(
            response,
            "/todolist/add/",
            target_status_code=302,
            fetch_redirect_response=False,
        )


class TodoListFormTests(TestCase):
    def setUp(self):
        self.vaild_form_data = {"title": "some title"}
        self.too_long_title = {"title": 129 * "X"}

    def test_valid_input(self):
        form = TodoListForm(self.vaild_form_data)
        self.assertTrue(form.is_valid())

    def test_no_title(self):
        form = TodoListForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {"title": ["This field is required."]})

    def test_empty_title(self):
        form = TodoListForm({"title": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {"title": ["This field is required."]})

    def test_too_long_title(self):
        form = TodoListForm(self.too_long_title)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {
                "title": [
                    "Ensure this value has at most 128 " + "characters (it has 129)."
                ]
            },
        )


class TodoFormTests(TestCase):
    def setUp(self):
        self.valid_form_data = {"description": "something to be done"}
        self.too_long_description = {"description": 129 * "X"}

    def test_valid_input(self):
        form = TodoForm(self.valid_form_data)
        self.assertTrue(form.is_valid())

    def test_no_description(self):
        form = TodoForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {"description": ["This field is required."]})

    def test_empty_description(self):
        form = TodoForm({"description": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {"description": ["This field is required."]})

    def test_too_title(self):
        form = TodoForm(self.too_long_description)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {
                "description": [
                    "Ensure this value has at most 128 " + "characters (it has 129)."
                ]
            },
        )


class ListModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("test", "test@example.com", "test")
        self.todolist = TodoList(title="title", creator=self.user)
        self.todolist.save()
        self.todo = Todo(
            description="description", todolist_id=self.todolist.id, creator=self.user
        )
        self.todo.save()

    def tearDown(self):
        self.todo.delete()
        self.todolist.delete()
        self.user.delete()

    def test_count_todos(self):
        self.assertEqual(self.todolist.count(), 1)
        new_todo = Todo(
            description="test", todolist_id=self.todolist.id, creator=self.user
        )
        new_todo.save()
        self.assertEqual(self.todolist.count(), 2)

    def test_count_open_todos(self):
        self.assertEqual(self.todolist.count_open(), 1)
        new_todo = Todo(
            description="test", todolist_id=self.todolist.id, creator=self.user
        )
        new_todo.save()
        self.assertEqual(self.todolist.count_open(), 2)
        new_todo.close()
        self.assertEqual(self.todolist.count_open(), 1)

    def test_count_closed_todos(self):
        self.assertEqual(self.todolist.count_finished(), 0)
        new_todo = Todo(
            description="test", todolist_id=self.todolist.id, creator=self.user
        )
        new_todo.close()
        self.todo.close()
        self.assertEqual(self.todolist.count_finished(), 2)
        self.assertIsNotNone(new_todo.finished_at)
        self.todo.reopen()
        self.assertEqual(self.todolist.count_finished(), 1)
        self.assertIsNone(self.todo.finished_at)
