from dataclasses import fields
from rest_framework import serializers
from .models import Todo,timeTodo

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Todo
		exclude = ['updated_at','created_at']


class TimingSerializer(serializers.ModelSerializer):
	class Meta:
		model = timeTodo
		exclude = ['updated_at','created_at']
