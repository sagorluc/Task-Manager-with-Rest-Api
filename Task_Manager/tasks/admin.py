from django.contrib import admin
from tasks.models import TaskModel, TaskImage

# Register your models here.
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'priority']
    ordering = ['id']

admin.site.register(TaskModel, TaskModelAdmin)
admin.site.register(TaskImage)