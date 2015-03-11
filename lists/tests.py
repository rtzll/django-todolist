from django.test import TestCase
from django.contrib.auth.models import User

from lists.forms import TodoForm, TodoListForm


class ListTests(TestCase):

    def setUp(self):
        User.objects.create_user('test', 'test@example.com', 'test')
        self.client.login(username='test', password='test')

    def tearDown(self):
        User.objects.get(username='test').delete()
        self.client.logout()

    def test_get_index_page(self):
        pass

    def test_add_todo_to_index_page(self):
        pass

    def test_get_todolist_view(self):
        pass

    def test_add_todo_to_todolist_view(self):
        pass

    def test_get_todolist_overview(self):
        pass

    def test_add_todolist_to_todolist_overview(self):
        pass


class TodoListFormTests(TestCase):

    def setUp(self):
        self.vaild_form_data = {
            'title': 'some title'
        }
        self.too_long_title = {
            'title': 129 * 'X'
        }

    def test_valid_input(self):
        form = TodoListForm(self.vaild_form_data)
        self.assertTrue(form.is_valid())

    def test_no_title(self):
        form = TodoListForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {'title': [u'This field is required.']}
        )

    def test_empty_title(self):
        form = TodoListForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {'title': [u'This field is required.']}
        )

    def test_too_title(self):
        form = TodoListForm(self.too_long_title)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {'title': [u'Ensure this value has at most 128 ' + \
                       'characters (it has 129).']}
        )


class TodoFormTests(TestCase):

    def setUp(self):
        self.valid_form_data = {
            'description': 'something to be done'
        }
        self.too_long_description = {
            'description': 129 * 'X'
        }

    def test_valid_input(self):
        form = TodoForm(self.valid_form_data)
        self.assertTrue(form.is_valid())

    def test_no_description(self):
        form = TodoForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {'description': [u'This field is required.']}
        )

    def test_empty_description(self):
        form = TodoForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {'description': [u'This field is required.']}
        )

    def test_too_title(self):
        form = TodoForm(self.too_long_description)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {'description': [u'Ensure this value has at most 128 ' + \
                             'characters (it has 129).']}
        )


class ListModelTests(TestCase):
    pass

