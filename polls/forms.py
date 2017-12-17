from django import forms

class TodoForm(forms.Form):
    todo_name = forms.CharField(label='',max_length=100,
                                widget=forms.TextInput(attrs={'placeholder': 'What\' to be done ?'})
    )