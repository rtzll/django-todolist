from django import forms
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from accounts.forms import LoginForm, RegistrationForm

MAIL_SAMPLE             = "test@example.com"
CONST_FIELD_REQUIRED    = "This field is required."
CONST_AUTH_REGISTER     = "auth:register"
CONST_AUTH_LOGIN        = "auth:login"
class AccountsTests(TestCase):
    def setUp(self):
        self.register_data = {
            "email": "new@user.com",
            "username": "new_user",
            "password": "test",
            "password_confirmation": "test",
        }
        User.objects.create_user("test", MAIL_SAMPLE , "test")

    def tearDown(self):
        User.objects.get(username="test").delete()

    def test_get_register(self):
        response = self.client.get(reverse(CONST_AUTH_REGISTER))
        self.assertTemplateUsed(response, "accounts/register.html")
        self.assertIsInstance(response.context["form"], RegistrationForm)

    def test_get_login(self):
        response = self.client.get(reverse(CONST_AUTH_LOGIN))
        self.assertTemplateUsed(response, "accounts/login.html")
        self.assertIsInstance(response.context["form"], LoginForm)

    def test_register(self):
        response = self.client.post(reverse(CONST_AUTH_REGISTER), data=self.register_data)
        self.assertRedirects(response, "/auth/login/")
        # new user was created
        self.assertIsNotNone(User.objects.get(username="new_user"))

    def test_login(self):
        # no user is logged in
        self.assertFalse("_auth_user_id" in self.client.session)
        login_data = {"username": "test", "password": "test"}
        response = self.client.post(reverse(CONST_AUTH_LOGIN), data=login_data)
        self.assertRedirects(response, "/")
        # user is logged in
        self.assertEqual(self.client.session["_auth_user_id"], "1")

    # check if error messages are part of the response
    def test_faulty_login(self):
        # change username for invalid post
        login_data = {"username": 65 * "X", "password": "test"}
        response = self.client.post(reverse(CONST_AUTH_LOGIN), data=login_data)
        error_message = "Ensure this value has at most 64 characters"
        self.assertContains(response, error_message, status_code=200)

    def test_login_with_non_existent_user(self):
        # change username for invalid post
        login_data = {"username": "notauser", "password": "stillapassowrd"}
        response = self.client.post(reverse(CONST_AUTH_LOGIN), data=login_data)
        error_message = "Incorrect username and/or password."
        self.assertContains(response, error_message, status_code=200)

    def test_login_with_wrong_password(self):
        # change username for invalid post
        login_data = {"username": "test", "password": "wrongpassword"}
        response = self.client.post(reverse(CONST_AUTH_LOGIN), data=login_data)
        error_message = "Incorrect username and/or password."
        self.assertContains(response, error_message, status_code=200)

    def test_faulty_register(self):
        # change username for invalid post
        self.register_data["username"] = 65 * "X"
        response = self.client.post(reverse(CONST_AUTH_REGISTER), data=self.register_data)
        error_message = "Ensure this value has at most 64 characters"
        self.assertContains(response, error_message, status_code=200)

    def test_logout(self):
        response = self.client.get(reverse("auth:logout"))
        self.assertRedirects(response, "/")
        # no user logged in anymore
        self.assertFalse("_auth_user_id" in self.client.session)


class LoginFormTests(TestCase):

    # valid test case is covered by AccountsTests (because we need a user)
    def setUp(self):
        self.too_long_password = {"username": "test", "password": 65 * "X"}
        self.too_long_username = {"username": 65 * "X", "password": "test"}

    def test_too_long_username(self):
        form = LoginForm(self.too_long_username)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {
                "username": [
                    "Ensure this value has at most 64" + " characters (it has 65)."
                ]
            },
        )

    def test_too_long_password(self):
        form = LoginForm(self.too_long_password)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {
                "password": [
                    "Ensure this value has at most 64" + " characters (it has 65)."
                ]
            },
        )

    def test_no_username(self):
        form = LoginForm({"password": "test"})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {"username": [CONST_FIELD_REQUIRED]})

    def test_no_password(self):
        form = LoginForm({"username": "test"})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {"password": [CONST_FIELD_REQUIRED]})

    def test_empty_username(self):
        form = LoginForm({"username": "", "password": "test"})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {"username": [CONST_FIELD_REQUIRED]})

    def test_empty_password(self):
        form = LoginForm({"username": "test", "password": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {"password": [CONST_FIELD_REQUIRED]})


class RegistrationFormTests(TestCase):
    def setUp(self):
        self.valid_form_data = {
            "email": MAIL_SAMPLE,
            "username": "test",
            "password": "test",
            "password_confirmation": "test",
        }
        self.invalid_email = {
            "email": "test(at)example.com",
            "username": "test",
            "password": "test",
            "password_confirmation": "test",
        }
        self.non_matching_passwords = {
            "email": MAIL_SAMPLE,
            "username": "test",
            "password": "test1",
            "password_confirmation": "test2",
        }

    # some tests can be skipped because of the coverage of LoginFormTests
    def test_valid_input(self):
        form = RegistrationForm(self.valid_form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_email(self):
        form = RegistrationForm(self.invalid_email)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {"email": ["Enter a valid email address."]})

    def test_non_matching_passwords(self):
        form = RegistrationForm(self.non_matching_passwords)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {"__all__": ["Passwords don't match."]})
