from rest_framework import serializers
from tasks.models import TaskModel

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ['user', 'title', 'description', 
                  'due_date', 'priority', 'complete', 
                  'created_at', 'updated_at'
                  ]