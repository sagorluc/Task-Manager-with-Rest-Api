from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CHOICES = [
    ('low', 'Low'), 
    ('medium', 'Medium'), 
    ('high', 'High')
]

class TaskModel(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='user')
    title = models.CharField(max_length= 100)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices= CHOICES)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        
    def __str__(self):
        return self.title
    
    
class TaskImage(models.Model):
    task = models.ForeignKey(TaskModel, on_delete=models.CASCADE, related_name= 'tasks')
    image = models.ImageField(upload_to='photos/tasks')
    
    class Meta:
        verbose_name = 'Task Image'
        verbose_name_plural = 'Task Images'
        
    def __str__(self):
        return self.task.title