from datetime import date
from time import time
import uuid
from django.db import models
from numpy import true_divide


# Create your models here.

class Task(models.Model):
    uid = models.UUIDField(primary_key= True,editable=False,default=uuid.uuid4())
    created_at = models.DateField(auto_created=True,default=date.today())
    updated_at = models.DateField(auto_created=True,default=date.today())
    
    class Meta:
        abstract = True

class Todo(Task):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False,blank=True,null=True)
