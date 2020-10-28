from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lists.models import TodoList


class UserTests(APITestCase):
    def setUp(self):
        User.objects.create_user("test", "test@example.com", "test")
        self.client.login(username="test", password="test")

    def tearDown(self):
        User.objects.get(username="test").delete()
        self.client.logout()

    def test_post_on_read_only(self):
        response = self.client.post("api:user-list", {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_user_if_not_admin(self):
        # get user (test user from setup)
        get_response = self.client.get("/api/users/{}/".format(1))
        self.assertEqual(get_response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_user_if_admin(self):
        # create admin user and login as such
        User.objects.create_superuser("admin", "admin@example.com", "admin")
        self.client.login(username="admin", password="admin")
        # get user (test user from setup)
        get_response = self.client.get("/api/users/{}/".format(1))
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        # check user
        self.assertEqual(get_response.data["username"], "test")


class TodoListTests(APITestCase):
    def setUp(self):
        User.objects.create_user("test", "test@example.com", "test")
        self.client.login(username="test", password="test")
        self.test_data = {"title": "some other title", "todos": []}

    def tearDown(self):
        User.objects.get(username="test").delete()
        self.client.logout()

    def post_new_todolist(self, data):
        url = reverse("api:todolist-list")
        return self.client.post(url, data, format="json")

    def test_create_todolist(self):
        response = self.post_new_todolist(self.test_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], self.test_data["title"])

    def test_get_todolist(self):
        # add todolist
        post_response = self.post_new_todolist(self.test_data)
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)
        # get todolist
        todolist_id = post_response.data["id"]
        self.assertEqual(todolist_id, 1)
        get_response = self.client.get(f"/api/todolists/{todolist_id}/")
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        # check todolist
        self.assertEqual(get_response.data, post_response.data)

    def test_get_when_not_logged_in(self):
        # add some data
        post_response = self.post_new_todolist(self.test_data)
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)
        # make sure the user is logged out
        self.client.logout()
        response = self.client.get("/api/todolists/1/")
        # expect 200, because reading is allowed for everybody
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_non_existent_todolist(self):
        response = self.client.get("/api/todolists/0/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_for_anon_users(self):
        # make sure the user is logged out
        self.client.logout()
        # try posting a todolist
        response = self.post_new_todolist(self.test_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_todolist(self):
        # add todolist
        post_response = self.post_new_todolist(self.test_data)
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)
        # put todolist
        todolist_id = post_response.data["id"]
        put_data = post_response.data
        put_data["title"] = "changed title"
        put_response = self.client.put(
            f"/api/todolists/{todolist_id}/", put_data, format="json"
        )
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        get_response = self.client.get(f"/api/todolists/{todolist_id}/")
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        self.assertEqual(get_response.data["title"], "changed title")

    def test_delete_todolist(self):
        # add todolist
        post_response = self.post_new_todolist(self.test_data)
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)
        # delete todolist
        todolist_id = post_response.data["id"]
        delete_response = self.client.delete(f"/api/todolists/{todolist_id}/")
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
        # get todolist and expect 404
        get_response = self.client.get(f"/api/todolists/{todolist_id}/")
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)


class TodoTests(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user("test", "test@example.com", "test")
        self.client.login(username="test", password="test")
        self.test_todolist = TodoList(title="some title", creator=self.test_user)
        self.test_todolist.save()
        self.test_data = {
            "description": "some description",
            "todolist": self.test_todolist.id,
        }

    def tearDown(self):
        test_user = User.objects.get(username="test")
        test_user.delete()
        self.client.logout()

    def post_new_todo(self, data):
        url = reverse("api:todo-list")
        return self.client.post(url, data, format="json")

    def test_create_todo(self):
        response = self.post_new_todo(self.test_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["description"], self.test_data["description"])

    def test_get_todo(self):
        # add todo
        post_response = self.post_new_todo(self.test_data)
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)
        # get todo
        todo_id = post_response.data["id"]
        self.assertEqual(todo_id, 1)
        get_response = self.client.get(f"/api/todos/{todo_id}/")
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        # check todo
        self.assertEqual(get_response.data, post_response.data)

    def test_get_when_not_logged_in(self):
        # add some data
        post_response = self.post_new_todo(self.test_data)
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)
        # make sure the user is logged out
        self.client.logout()
        response = self.client.get("/api/todos/1/")
        # expect 200, because reading is allowed for everybody
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_non_existent_todo(self):
        response = self.client.get("/api/todo/0/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_for_anon_users(self):
        # make sure the user is logged out
        self.client.logout()
        # try posting a todo
        response = self.post_new_todo(self.test_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_todo(self):
        # add todo
        post_response = self.post_new_todo(self.test_data)
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)
        # put todo
        todo_id = post_response.data["id"]
        put_data = post_response.data
        put_data["description"] = "changed description"
        put_response = self.client.put(
            f"/api/todos/{todo_id}/", put_data, format="json"
        )
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        get_response = self.client.get(f"/api/todos/{todo_id}/")
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        self.assertEqual(get_response.data["description"], "changed description")

    def test_put_todo_changing_status(self):
        # add todo
        post_response = self.post_new_todo(self.test_data)
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)
        # put todo
        todo_id = post_response.data["id"]
        put_data = post_response.data
        put_data["is_finished"] = True
        put_response = self.client.put(
            f"/api/todos/{todo_id}/", put_data, format="json"
        )
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        get_response = self.client.get(f"/api/todos/{todo_id}/")
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        self.assertEqual(get_response.data["is_finished"], True)

    def test_delete_todo(self):
        # add todo
        post_response = self.post_new_todo(self.test_data)
        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)
        # delete todolist
        todo_id = post_response.data["id"]
        delete_response = self.client.delete(f"/api/todos/{todo_id}/")
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
        # get todolist and expect 404
        get_response = self.client.get(f"/api/todos/{todo_id}/")
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)
