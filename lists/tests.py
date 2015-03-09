from django.test import TestCase


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


class ListFormsTests(TestCase):
    pass


class ListModelTests(TestCase):
    pass
