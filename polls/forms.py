from django import forms
import datetime

class TodoForm(forms.Form):
    todo_name = forms.CharField(label='',max_length=100,
                                widget=forms.TextInput(attrs={'placeholder': 'What\' to be done ?'})
    )
    expired_date = forms.DateField(initial=datetime.date.today,required=False)