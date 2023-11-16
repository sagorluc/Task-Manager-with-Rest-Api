from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from tasks.models import TaskModel
from api_view.serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import authenticate
# Create your views here.

class TaskListCreateAPIView(ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return TaskModel.objects.filter(user= self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(user= self.request.user)
    
    # def get_serializer_class(self):
    #     if self.request.method == 'POST':
    #         return CreateTaskSerializer
    #     else:
    #         return TaskSerializer
            
    

class TaskRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    # queryset         = TaskModel.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return TaskModel.objects.filter(user= self.request.user)
