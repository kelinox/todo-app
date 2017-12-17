from django.db import models
import datetime

# Create your models here.

class Todo(models.Model):
    todo_text = models.CharField(max_length=200,primary_key=True)
    validate = models.BooleanField(default=False)

    def __str__(self):
        return "You have to "+self.todo_text+" validate : "+str(self.validate)