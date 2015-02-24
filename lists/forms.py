from django import forms


class TodoForm(forms.Form):
    description = forms.CharField(max_length=128, widget=forms.TextInput(
        attrs={'class': 'u-full-width', 'placeholder': 'Enter your todo'}))


class TodoListForm(forms.Form):
    title = forms.CharField(max_length=128)
