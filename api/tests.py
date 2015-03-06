from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TodoListTests(APITestCase):

    def test_get_todolist(self):
        # add todolist
        # get todolist
        # check todolist
        pass

    def test_create_todolist(self):
        url = reverse('api:todolist-list')
        data = {'title': 'some title'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)
