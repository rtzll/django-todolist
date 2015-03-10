from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django import forms

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


class LoginFormTests(TestCase):

    def setUp(self):
        self.valid_form_data = {'username': 'test', 'password': 'test'}
        self.too_long_password = {'username': 'test', 'password': 65 * 'X'}
        self.too_long_username = {'username': 65 * 'X', 'password': 'test'}

    def test_valid_input(self):
        form = LoginForm(self.valid_form_data)
        self.assertTrue(form.is_valid())

    def test_too_long_username(self):
        # python 3.5 {**valid_username_dict, **invalid_password_dict}
        form = LoginForm(self.too_long_username)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {'username': [u'Ensure this value has at most 64' +\
                          ' characters (it has 65).']}
        )

    def test_too_long_password(self):
        form = LoginForm(self.too_long_password)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {'password': [u'Ensure this value has at most 64' +\
                          ' characters (it has 65).']}
        )

    def test_no_username(self):
        form = LoginForm({'password': 'test'})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {'username': [u'This field is required.']}
        )

    def test_no_password(self):
        form = LoginForm({'username': 'test'})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {'password': [u'This field is required.']}
        )

    def test_empty_username(self):
        form = LoginForm({'username': '', 'password': 'test'})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {'username': [u'This field is required.']}
        )

    def test_empty_password(self):
        form = LoginForm({'username': 'test', 'password': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {'password': [u'This field is required.']}
        )


class RegistrationFormTests(TestCase):
    pass
