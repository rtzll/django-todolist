from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='', max_length=64,
        widget=forms.TextInput(
            attrs={'class': 'u-full-width', 'placeholder': 'Username'}))
    password = forms.CharField(label='', max_length=64,
        widget=forms.PasswordInput(
            attrs={'class': 'u-full-width', 'placeholder': 'Password'}))


class RegistrationForm(forms.Form):
    email = forms.EmailField(label='', max_length=64, widget=forms.TextInput(
        attrs={'class': 'u-full-width', 'placeholder': 'Email'}))

    username = forms.CharField(label='', max_length=64,
        widget=forms.TextInput(
            attrs={'class': 'u-full-width', 'placeholder': 'Username'}))

    password = forms.CharField(label='', max_length=64,
        widget=forms.PasswordInput(
            attrs={'class': 'u-full-width', 'placeholder': 'Password'}))

    password_confirmation = forms.CharField(
        label='', max_length=64, widget=forms.PasswordInput(
            attrs={'class': 'u-full-width',
                   'placeholder': 'Password confirmation'}))
