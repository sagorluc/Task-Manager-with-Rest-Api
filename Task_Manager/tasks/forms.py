from django import forms
from tasks.models import TaskModel, TaskImage
from django.forms import ClearableFileInput


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['title', 'description', 'due_date', 'priority', 'complete']

    def __init__(self, user, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields.pop('user', None) # Remove the user from user form
        self.user = user
        self.fields['title'].widget.attrs['placeholder'] = 'Enter Title'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter Description..'
        self.fields['due_date'].widget.attrs['placeholder'] = 'Enter Date D/M/Y'

    def save(self, commit=True):
        instance = super(TaskForm, self).save(commit=False)
        instance.user = self.user

        if commit:
            instance.save()

        uploaded_images = self.cleaned_data.get('images' , [])
        for image in uploaded_images:
            task_image = TaskImage(task=instance, image=image)
            task_image.save()

        return instance
       
        
        
class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=100, required=False)
    
    
    
class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model   = TaskModel
        fields  = ['title', 'description', 'due_date', 'priority', 'complete']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }


    # Set the image 
    def save(self, commit=True):
        instance = super().save(commit=False)
        images   = self.cleaned_data.get('images', []) # Multiple images from input field
        
        if commit:
            instance.save()
        
        for image in images:
            task_image = TaskImage(task=instance, image=image)
            task_image.save()

        return instance
    
    # placeholder by overiding
    def __init__(self, *args, **kwargs):
        super(TaskUpdateForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Enter Title'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter Description..'
        self.fields['due_date'].widget.attrs['placeholder'] = 'Enter Date D/M/Y'

        
        
class TaskFilterForm(forms.Form):
    priority   = forms.CharField(max_length=10, required=False)
    complete   = forms.BooleanField(required=False)
    due_date   = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    created_at = forms.DateTimeField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))