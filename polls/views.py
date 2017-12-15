from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_protect

from .models import Todo
from .forms import TodoForm

from django.views.decorators.csrf import csrf_exempt

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
                error = "no"
            except IntegrityError as e:
                error = "yes"
        else:
            error = "yes"

        return HttpResponse(json.dumps({
                            'todo_name': todo_name,
                            'error': error,
        }))
    else:
        form = TodoForm()

    context = {
        'todo_list': todo_list,
        'form': form,
    }
    return render(request,'polls/index.html',context)

def delete(request):
    remove = "Error while removing"
    if request.method == 'POST':
        remove="deleted"
        t = Todo.objects.get(todo_text=request.POST['text'])
        t.delete()
        remove = "Successfuly removed the task"
    return HttpResponse(json.dumps({
                        'message': remove
                    }))
    
def validate(request):
    if request.method == 'POST':
        t = Todo.objects.get(todo_text=request.POST['text'])
        t.validate = True
        t.save()
    return HttpResponse(json.dumps({
                        'message':'Successfuly validate the task'
                    }))

# Create your views here.
