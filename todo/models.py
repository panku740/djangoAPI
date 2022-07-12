from datetime import date
from time import time
import uuid
from django.db import models
from numpy import true_divide


# Create your models here.

class Task2(models.Model):
    uid = models.UUIDField(primary_key= True,editable=False,unique=True,default=uuid.uuid4)
    created_at = models.DateField(auto_created=True,default=date.today())
    updated_at = models.DateField(auto_created=True,default=date.today())
    
    class Meta:
        abstract  = True

class Todo(Task2):
    title = models.CharField(max_length=200)
    Desc = models.CharField(max_length=200)
    completed = models.BooleanField(default=False,blank=True,null=True)
    

class timeTodo(Task2):
    todo = models.ForeignKey(Todo,on_delete=models.CASCADE)
    timing = models.DateField()