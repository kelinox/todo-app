from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Todo

def index(request):
    todo_list = Todo.objects.order_by('-expired_date')[:5]
    context = {
        'todo_list': todo_list,
    }
    return render(request,'polls/index.html',context)
    

# Create your views here.
