from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader

from .models import Todo
from .forms import TodoForm

def index(request):
    todo_list = Todo.objects.order_by('-expired_date')[:5]
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo_name = form.cleaned_data['todo_name']
            expired_date = form.cleaned_data['expired_date']
            todo = Todo(todo_text=todo_name,expired_date=expired_date)
            todo.save()
        else:
            todo_name = "Not clean"
            expired_date = "Not clean"
    else:
        form = TodoForm()
        todo_name = "null"
        expired_date = "Null"

    context = {
        'todo_list': todo_list,
        'form': form,
        'todo_name': todo_name,
        'expired_date': expired_date,
    }
    return render(request,'polls/index.html',context)
    

# Create your views here.
