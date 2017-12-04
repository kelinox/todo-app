from django.shortcuts import render
from django.http import HttpResponse

from .models import Todo

def index(request):
    todo_list = Todo.objects.order_by('-expired_date')[:5]
    output = ','.join([t.todo_text for t in todo_list])
    return HttpResponse(output)
    

# Create your views here.
