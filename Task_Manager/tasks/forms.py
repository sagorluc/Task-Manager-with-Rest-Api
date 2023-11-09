from django import forms
from tasks.models import TaskModel, TaskImage

class TaskForm(forms.ModelForm):
    class Meta:
        model  = TaskModel
        fields = ['user', 'title', 'description', 'due_date', 'priority', 'complete']
    
    # set placeholder    
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Enter Title'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter Description..'
        self.fields['due_date'].widget.attrs['placeholder'] = 'Enter Date D/M/Y'
       
        
        
class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=100, required=False)
    
    
class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model   = TaskModel
        fields  = ['user', 'title', 'description', 'due_date', 'priority', 'complete']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }

    image = forms.ImageField(required=False)    # image field can be blank

    # Image field label
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].label = 'Image'

    # Set the image 
    def save(self, commit=True):
        instance = super().save(commit=False)
        image    = self.cleaned_data.get('image')
        if image:
            task_image = TaskImage(task=instance, image=image)
            task_image.save()
        if commit:
            instance.save()
        return instance
    
    # set placeholder
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