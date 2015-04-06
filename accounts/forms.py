from django import forms


def widget_attrs(placeholder):
    return {'class': 'u-full-width', 'placeholder': placeholder}


def forms_kwargs(widget, label='', max_length=64):
    return {'widget': widget, 'label': label, 'max_length': max_length}


class LoginForm(forms.Form):

    username = forms.CharField(
        forms_kwargs(widget=forms.TextInput(attrs=widget_attrs('Username')))
    )
    password = forms.CharField(
        forms_kwargs(
            widget=forms.PasswordInput(attrs=widget_attrs('Password'))
        )
    )


class RegistrationForm(forms.Form):

    email = forms.EmailField(
        forms_kwargs(widget=forms.TextInput(attrs=widget_attrs('Email')))
    )
    username = forms.CharField(
        forms_kwargs(widget=forms.TextInput(attrs=widget_attrs('Username')))
    )

    password = forms.CharField(
        forms_kwargs(
            widget=forms.PasswordInput(attrs=widget_attrs('Password'))
        )
    )
    password_confirmation = forms.CharField(
        forms_kwargs(
            widget=forms.PasswordInput(
                attrs=widget_attrs('Password confirmation')
            )
        )
    )

    def clean(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if password and password != password_confirmation:
            raise forms.ValidationError("Passwords don't match.")

        return self.cleaned_data
