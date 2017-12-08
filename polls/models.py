from django.db import models
import datetime

# Create your models here.

class Todo(models.Model):
    todo_text = models.CharField(max_length=200,primary_key=True)
    day_left = models.IntegerField()

    def __str__(self):
        return "You have to "+self.todo_text+" before "+str(self.day_left)