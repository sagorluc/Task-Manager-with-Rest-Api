from django.urls import path
from tasks.views import CreateTask, IncompleteTask, UpdateTask, TaskDelete, TaskDetail, \
    CompleteTask, ShowAllTask,  SearchTask, DeleteImageView

urlpatterns = [
    path('create/', CreateTask.as_view(), name= 'create'),
    path('incomplete_task/', IncompleteTask.as_view(), name= 'show_task'),
    path('show_all_tasks/', ShowAllTask.as_view(), name= 'all_tasks'),
    path('update_task/<int:id>/', UpdateTask.as_view(), name= 'update_task'),
    path('delete_task/<int:id>/', TaskDelete.as_view(), name= 'delete_task'),
    path('delete_image/<int:id>/', DeleteImageView.as_view(), name= 'delete_image'),
    path('detail_task/<int:id>/', TaskDetail.as_view(), name= 'detail_task'),
    path('complate_task/<int:id>/', CompleteTask.as_view(), name= 'complate_task'),
    path('search/', SearchTask.as_view(), name= 'search'),
   
   
]
