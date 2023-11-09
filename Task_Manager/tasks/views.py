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
    # success_url = reverse_lazy('show_task')
    
    def form_valid(self, form):
        # initial completeness set kora holo based on the form submission
        self.object = form.save(commit=False)
        if self.object.complete:
            return super().form_valid(form)
        else:
            return super().form_valid(form)

    def get_success_url(self):
        if self.object.complete:
            return reverse_lazy('complate_task', kwargs={'id': self.object.id})
        else:
            return reverse_lazy('show_task')
        
        


@method_decorator(login_required, name='dispatch')
class ShowAllTask(ListView):
    model = TaskModel
    template_name = 'show_task.html'
    context_object_name = 'tasks'
    
    
    

@method_decorator(login_required, name='dispatch') 
class CompleteTask(ListView):
    model = TaskModel
    template_name = 'complate_tasks.html'
    context_object_name = 'complete_tasks'

    def get_queryset(self):
        # task er complete true set kora holo
        TaskModel.objects.filter(pk=self.kwargs['id']).update(complete=True)
        
        # complete true return kora holo
        return TaskModel.objects.filter(complete=True)
    
    
    
      
@method_decorator(login_required, name='dispatch') 
class UpdateTask(UpdateView):
    model = TaskModel
    form_class = TaskUpdateForm
    template_name = 'update_task.html'
    pk_url_kwarg = 'id'
    context_object_name = 'task'

    def form_valid(self, form):
        return super().form_valid(form)
    
    
    def get_success_url(self):
        if 'show_task' in self.request.META.get('HTTP_REFERER', ''):
            return reverse_lazy('show_task')
        elif 'complate_task' in self.request.META.get('HTTP_REFERER', ''):
            return reverse_lazy('complate_task', kwargs={'id': self.kwargs['id']})
        else:
            return reverse_lazy('search')
        
        
    

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
        queryset = TaskModel.objects.all()

        if keyword:
            queryset = queryset.filter(Q(title__icontains=keyword) | Q(priority__icontains=keyword))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm(self.request.GET)
        return context
    
    

  
@method_decorator(login_required, name='dispatch')
class FilterTask(View):
    template_name = 'filter_task.html'
    form_class = TaskFilterForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            priority = form.cleaned_data['priority']
            complete = form.cleaned_data['complete']
            due_date = form.cleaned_data['due_date']
            created_at = form.cleaned_data['created_at']
            
            tasks = TaskModel.objects.all()

            if priority:
                tasks = tasks.filter(priority__icontains=priority)
            if complete is not None:
                tasks = tasks.filter(complete=complete)
            if due_date:
                tasks = tasks.filter(due_date=due_date)
            if created_at:
                tasks = tasks.filter(created_at=created_at)

            context = {'tasks': tasks}
            return render(request, 'filter_task.html', context)

        return render(request, self.template_name, {'form': form})
    