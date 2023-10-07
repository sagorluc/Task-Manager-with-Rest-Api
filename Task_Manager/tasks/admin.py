from django.contrib import admin
from tasks.models import TaskModel, TaskImage

# Register your models here.
admin.site.register(TaskModel)
admin.site.register(TaskImage)