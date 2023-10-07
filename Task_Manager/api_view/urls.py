from django.urls import path
from api_view.views import TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', TaskListCreateAPIView.as_view(), name='create_api'), # Read and Create url
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='all_api'), # retrieve, Update, Delete
]