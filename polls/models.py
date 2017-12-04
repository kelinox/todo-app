from django.db import models

# Create your models here.

class Todo(models.Model):
    todo_text = models.CharField(max_length=200)
    expired_date = models.DateTimeField('date expire')