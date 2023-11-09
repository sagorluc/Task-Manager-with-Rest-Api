from typing import Any
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    # chaeck the both passowrd is matched 
    def clean(self):
        cleaned_data     = super(RegistrationFrom, self).clean()
        password         = cleaned_data.get('password1')
        confirm_password = cleaned_data.get('password2')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )

    def __init__(self, *args, **kwargs):
        super(RegistrationFrom, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Username'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        
        
class LoginForm(AuthenticationForm):
    class Meta:
        model  = User
        fields = ['username', 'password']
        
    def clean(self):
        cleaned_data =  super(LoginForm, self).clean()
        username     = cleaned_data.get('username')
        password     = cleaned_data.get('password')
        
        user = User.objects.filter(username = username).first()
        
        if not user or not user.check_password(password):
            raise forms.ValidationError('Invalid username or password')
        
        return cleaned_data