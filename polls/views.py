from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
from django.db import IntegrityError

from .models import Todo
from .forms import TodoForm

def index(request):
    todo_list = Todo.objects.order_by('todo_text')
    if request.method == 'POST':
        form = TodoForm(request.POST)
        todo_name=""
        todo_id=len(Todo.objects.all())
        error = ""
        if form.is_valid():
            todo_name = form.cleaned_data['todo_name']
            day_left = form.cleaned_data['day_left']
            try:
                todo = Todo.objects.create(todo_text=todo_name,day_left=day_left)
                todo.save()
                todo_id += 1
            except IntegrityError as e:
                error = "already in the database"


        return HttpResponse(json.dumps({
                            'todo_name': todo_name,
                            'todo_id': todo_id,
                            'error': error,
        }))
    else:
        form = TodoForm()

    context = {
        'todo_list': todo_list,
        'form': form,
    }
    return render(request,'polls/index.html',context)
    

# Create your views here.
