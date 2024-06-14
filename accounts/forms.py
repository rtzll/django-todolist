from django import forms
from django.contrib.auth.models import User


def widget_attrs(placeholder):
    return {"class": "u-full-width", "placeholder": placeholder}


def form_kwargs(widget, label="", max_length=64):
    return {"widget": widget, "label": label, "max_length": max_length}


class LoginForm(forms.Form):

    username = forms.CharField(
        **form_kwargs(widget=forms.TextInput(attrs=widget_attrs("Username")))
    )
    password = forms.CharField(
        **form_kwargs(widget=forms.PasswordInput(attrs=widget_attrs("Password")))
    )

    def clean(self):
        # Don't check if we already have errors.
        if self.errors:
            return self.cleaned_data

        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = User.objects.filter(username=username).first()

        if not user or not user.check_password(password):
            raise forms.ValidationError("Incorrect username and/or password.")

        return self.cleaned_data


class RegistrationForm(forms.Form):

    username = forms.CharField(
        **form_kwargs(widget=forms.TextInput(attrs=widget_attrs("Username")))
    )

    email = forms.EmailField(
        **form_kwargs(widget=forms.TextInput(attrs=widget_attrs("Email")))
    )

    password = forms.CharField(
        **form_kwargs(widget=forms.PasswordInput(attrs=widget_attrs("Password")))
    )

    password_confirmation = forms.CharField(
        **form_kwargs(
            widget=forms.PasswordInput(attrs=widget_attrs("Password confirmation"))
        )
    )

    def validate_password_strength(self, password):
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError("Password must contain at least one digit.")
        if not any(char.islower() for char in password):
            raise forms.ValidationError("Password must contain at least one lowercase letter.")
        if not any(char.isupper() for char in password):
            raise forms.ValidationError("Password must contain at least one uppercase letter.")

    def clean(self):
        password = self.cleaned_data.get("password")
        password_confirmation = self.cleaned_data.get("password_confirmation")

        if password:
            self.validate_password_strength(password)
            if password != password_confirmation:
                raise forms.ValidationError("Passwords don't match.")

        return self.cleaned_data


