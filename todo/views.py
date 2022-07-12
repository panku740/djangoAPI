

from argparse import Action
from logging import exception
from urllib import response
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import TaskSerializer, TimingSerializer
from .models import Todo, timeTodo
from rest_framework import viewsets

 
class todoViewSet(viewsets.ModelViewSet):
    print ("test")
    queryset = Todo.objects.all()
    serializer_class = TaskSerializer

    @action(detail=False,methods=['GET'])
    def show_Date(self,request):
        
        data = timeTodo.objects.all()
        serializer = TimingSerializer(data ,many = True)
        
        return Response({
            'status':True,
            'message':'success',
            'data':serializer.data
        })


    @action(detail=False, methods=['POST'])
    def add_Date(self,request):
        
        try:
            data = request.data
            serializer = TimingSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':True,
                    'message':'success',
                    'data':serializer.data
                })
            return Response({
                'status':False,
                'message':'invalid data',
                'data':serializer.errors
            })    

        except exception as e:
            print(e)     

        return Response({
            'status': False,
            'message':'Something went Wrong.'
        })
    
             



