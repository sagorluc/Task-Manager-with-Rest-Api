from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from tasks.models import TaskModel, TaskImage
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, RedirectView
from tasks.forms import TaskForm, SearchForm, TaskUpdateForm, TaskFilterForm
from django.contrib import messages
from django.db.models import Q
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(login_required, name='dispatch')
class CreateTask(CreateView):
    model = TaskModel
    form_class = TaskForm
    template_name = 'create_task.html'
    context_object_name = 'create'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)

        images = self.request.FILES.getlist('images')
        for image in images:
            task_image = TaskImage(task=form.instance, image=image)
            task_image.save()

        return response

    def get_success_url(self):
        return reverse_lazy('all_tasks')
   
        
        
class ShowAllTask(ListView):
    model = TaskModel
    template_name = 'show_all_tasks.html'
    context_object_name = 'all_tasks'
    
    def get_queryset(self):
        return TaskModel.objects.filter(user= self.request.user)
    
    
    def get(self, request, *args, **kwargs):
        priority_filter = request.GET.get('priority', '')
        complete_filter = request.GET.get('complete', '')
        due_date_filter = request.GET.get('due_date', '')
        created_at_filter = request.GET.get('created_at', '')

        # filter conditions
        filter_conditions = {} # keep in the empty dictionary
        if priority_filter:
            filter_conditions['priority'] = priority_filter
        if complete_filter:
            filter_conditions['complete'] = complete_filter
        if due_date_filter:
            filter_conditions['due_date'] = due_date_filter
        if created_at_filter:
            filter_conditions['created_at'] = created_at_filter

        # filter conditions useing database
        filtered_tasks = TaskModel.objects.filter(**filter_conditions, user= self.request.user)

        context = {'all_tasks': filtered_tasks}
        return render(request, self.template_name, context)
    
    
       

@method_decorator(login_required, name='dispatch')
class IncompleteTask(ListView):
    model = TaskModel
    template_name = 'incomplete_task.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return TaskModel.objects.filter(user= self.request.user)
        

    
@method_decorator(login_required, name='dispatch') 
class CompleteTask(ListView):
    model = TaskModel
    template_name = 'complate_tasks.html'
    context_object_name = 'complete_tasks'

    def get_queryset(self):
        # task er complete true set kora holo
        TaskModel.objects.filter(user= self.request.user, pk=self.kwargs['id']).update(complete=True)
        
        # complete true return kora holo
        return TaskModel.objects.filter(user= self.request.user, complete=True)
    
    
    
      
@method_decorator(login_required, name='dispatch') 
class UpdateTask(UpdateView):
    model = TaskModel
    form_class = TaskUpdateForm
    template_name = 'update_task.html'
    pk_url_kwarg = 'id'
    context_object_name = 'task'

    def form_valid(self, form):
        
        images = self.request.FILES.getlist('images')
        for image in images:
            task_image = TaskImage(task=form.instance, image=image)
            task_image.save()

        return super().form_valid(form)
    
    
    def get_success_url(self):
        return reverse_lazy('all_tasks')
    
        
        
        
@method_decorator(login_required, name='dispatch')
class TaskDelete(DeleteView):
    model = TaskModel
    template_name = 'delete_task.html'
    context_object_name = 'task'
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        task = self.get_object()  # ei object er task ke delete kora hobe
        if task.complete:
            return reverse_lazy('complate_task', kwargs={'id': task.id})
        else:
            return reverse_lazy('show_task')
        
        
        
        
@method_decorator(login_required, name='dispatch')        
class DeleteImageView(View):
    def get(self, request, id):
        image = get_object_or_404(TaskImage, id=id)
        image.delete()
        task_id  = image.task.id # get the task id
        return redirect('detail_task', task_id) # detail_task page e redirect hobe
    


    
@method_decorator(login_required, name='dispatch')  
class TaskDetail(DetailView):
    model = TaskModel
    template_name = 'more_info.html'
    pk_url_kwarg = 'id'
    context_object_name = 'info'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.get_object()
        task_images = task.tasks.all()
        context['task_images'] = task_images
        return context
    

  
    
@method_decorator(login_required, name='dispatch')  
class SearchTask(ListView):
    model = TaskModel
    template_name = 'search_task.html'  
    context_object_name = 'persons' 

    def get_queryset(self):
        keyword = self.request.GET.get('keyword', '')
        queryset = TaskModel.objects.filter(user= self.request.user)

        if keyword:
            queryset = queryset.filter(Q(title__icontains=keyword) | Q(priority__icontains=keyword))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm(self.request.GET)
        return context
    
    