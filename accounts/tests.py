from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from accounts.forms import RegistrationForm, LoginForm

class AccountsTests(TestCase):

    def setUp(self):
        User.objects.create_user('test', 'test@example.com', 'test')

    def tearDown(self):
        User.objects.get(username='test').delete()

    def test_get_register(self):
        response = self.client.get(reverse('auth:register'))
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.assertIsInstance(response.context['form'], RegistrationForm)

    def test_get_login(self):
        response = self.client.get(reverse('auth:login'))
        self.assertTemplateUsed(response, 'accounts/login.html')
        self.assertIsInstance(response.context['form'], LoginForm)

    def test_register(self):
        register_data = {
            'email': 'new@user.com',
            'username': 'new_user',
            'password': 'test',
            'password_confirmation': 'test'
        }
        response = self.client.post(
            reverse('auth:register'), data=register_data
        )
        self.assertEqual(response.status_code, 302)
        # new user was created
        self.assertIsNotNone(User.objects.get(username='new_user'))

    def test_login(self):
        # no user is logged in
        self.assertFalse('_auth_user_id' in self.client.session)
        login_data = {'username': 'test', 'password': 'test'}
        response = self.client.post(reverse('auth:login'), data=login_data)
        self.assertEqual(response.status_code, 302)
        # user is logged in
        self.assertEqual(self.client.session['_auth_user_id'], 1)

    # TODO add erroneous test cases for login and register (invalid data)
    # check if correct error is displayed/ form.errors is correct

    def test_logout(self):
        response = self.client.get(reverse('auth:logout'))
        self.assertEqual(response.status_code, 302)
        # no user logged in anymore
        self.assertFalse('_auth_user_id' in self.client.session)


# TODO add class testing the forms specifically
class AccountFormsTests(TestCase):
    pass
