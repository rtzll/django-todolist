from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase



class TodoListTests(APITestCase):

    def setUp(self):
        User.objects.create_user('test', 'test@example.com', 'test')
        self.client.login(username='test', password='test')

    def tearDown(self):
        test_user = User.objects.get(username='test')
        test_user.delete()
        self.client.logout()

    def post_new_todolist(self, data):
        url = reverse('api:todolist-list')
        return self.client.post(url, data, format='json')

    def test_create_todolist(self):
        data = {'title': 'some title', 'todos': []}
        response = self.post_new_todolist(data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])

    def test_get_todolist(self):
        data = {'title': 'some other title', 'todos': []}
        # add todolist
        post_response = self.post_new_todolist(data)
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)
        # get todolist
        todolist_id = post_response.data['id']
        self.assertEqual(todolist_id, 1)
        get_response = self.client.get(
            '/api/todolists/{0}/'.format(todolist_id))
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        # check todolist
        self.assertEqual(get_response.data, post_response.data)
