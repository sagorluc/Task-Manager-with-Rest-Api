from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from tasks.models import TaskModel
from api_view.serializers import TaskSerializer

# Create your views here.

class TaskListCreateAPIView(ListCreateAPIView):
    queryset         = TaskModel.objects.all()
    serializer_class = TaskSerializer
    

class TaskRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset         = TaskModel.objects.all()
    serializer_class = TaskSerializer
