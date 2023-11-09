from django.urls import path
from tasks.views import CreateTask, ShowAllTask, UpdateTask, TaskDelete, TaskDetail, \
    CompleteTask,  SearchTask, FilterTask, DeleteImageView

urlpatterns = [
    path('create/', CreateTask.as_view(), name= 'create'),
    path('show_task/', ShowAllTask.as_view(), name= 'show_task'),
    path('update_task/<int:id>/', UpdateTask.as_view(), name= 'update_task'),
    path('delete_task/<int:id>/', TaskDelete.as_view(), name= 'delete_task'),
    path('delete_image/<int:id>/', DeleteImageView.as_view(), name= 'delete_image'),
    path('detail_task/<int:id>/', TaskDetail.as_view(), name= 'detail_task'),
    path('complate_task/<int:id>/', CompleteTask.as_view(), name= 'complate_task'),
    path('search/', SearchTask.as_view(), name= 'search'),
    path('filter/', FilterTask.as_view(), name= 'filter'),
   
]
