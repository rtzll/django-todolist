from django import forms


def widget_attrs(placeholder):
    return {'class': 'u-full-width', 'placeholder': placeholder}


class TodoForm(forms.Form):
    description = forms.CharField(max_length=128,
        widget=forms.TextInput(attrs=widget_attrs('Enter your todo')))


class TodoListForm(forms.Form):
    title = forms.CharField(max_length=128, widget=forms.TextInput(
        attrs=widget_attrs('Enter a title to start a new todolist')))
