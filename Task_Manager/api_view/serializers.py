from rest_framework import serializers
from tasks.models import TaskModel, TaskImage
from django.contrib.auth.models import User


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['id']

        

class TaskSerializer(serializers.ModelSerializer):
    user   = CustomUserSerializer(read_only= True) # hide user from input
    images = serializers.ListField(child=serializers.ImageField(), write_only=True, required=False)
    
    class Meta:
        model  = TaskModel
        fields = ['user', 'title', 'description', 
                  'due_date', 'priority', 'complete', 
                  'created_at', 'updated_at', 'images'
                  ]
        