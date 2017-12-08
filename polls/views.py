from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import date
import json

from .models import Todo
from .forms import TodoForm

def index(request):
    todo_list = Todo.objects.order_by('+id')
    error = ""
    if request.method == 'POST':
        form = TodoForm(request.POST)
        todo_name=""
        todo_id=""
        if form.is_valid():
            expired_date = form.cleaned_data['expired_date']
            date_today = date.today()
            if expired_date > date_today:
                todo_name = form.cleaned_data['todo_name']
                todo = Todo(todo_text=todo_name,expired_date=expired_date)
                todo.save()
            else:
                error = "You can't add a todo with this date"
        else:
            error="Form not clean"

        return HttpResponse(json.dumps({
                            'todo_name': todo_name,
                            'todo_id': todo.id,
        }))
    else:
        form = TodoForm()

    context = {
        'todo_list': todo_list,
        'form': form,
        'error': error,
    }
    return render(request,'polls/index.html',context)
    

# Create your views here.
