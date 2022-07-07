

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task2
from rest_framework import viewsets

 
class todoViewSet(viewsets.ModelViewSet):
    print ("test")
    queryset = Task2.objects.all()
    serializer_class = TaskSerializer

