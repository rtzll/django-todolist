from django import forms


def widget_attrs(placeholder):
    return {'class': 'u-full-width', 'placeholder': placeholder}


class LoginForm(forms.Form):
    username = forms.CharField(label='', max_length=64,
        widget=forms.TextInput(attrs=widget_attrs('Username')))
    password = forms.CharField(label='', max_length=64,
        widget=forms.PasswordInput(attrs=widget_attrs('Password')))


class RegistrationForm(forms.Form):
    email = forms.EmailField(label='', max_length=64,
        widget=forms.TextInput(attrs=widget_attrs('Email')))
    username = forms.CharField(label='', max_length=64,
        widget=forms.TextInput(attrs=widget_attrs('Username')))
    password = forms.CharField(label='', max_length=64,
        widget=forms.PasswordInput(attrs=widget_attrs('Password')))
    password_confirmation = forms.CharField(label='', max_length=64,
        widget=forms.PasswordInput(attrs=widget_attrs('Password confirmation')
    ))

    def clean(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if password and password != password_confirmation:
            raise forms.ValidationError("Passwords don't match")

        return self.cleaned_data