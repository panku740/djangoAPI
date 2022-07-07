

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Todo

 
@api_view(['GET'])
def taskList(request):
	tasks = Todo.objects.all()
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()



	return Response(serializer.data)

