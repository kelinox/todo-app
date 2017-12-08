from django.db import models
import datetime

# Create your models here.

class Todo(models.Model):
    todo_text = models.CharField(max_length=200)
    expired_date = models.DateTimeField('date expire')

    def __str__(self):
        return "You have to "+self.todo_text+" before "+self.expired_date.strftime('%m/%d/%Y')