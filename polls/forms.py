from django import forms
import datetime

class TodoForm(forms.Form):
    todo_name = forms.CharField(label='Todo : ',max_length=100)
    expired_date = forms.DateField(initial=datetime.date.today,required=False)