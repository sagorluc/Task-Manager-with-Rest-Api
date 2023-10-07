from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from authentication.forms import RegistrationFrom, LoginForm
from django.urls import reverse_lazy
from django.views import View

# Create your views here.
class Registration(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegistrationFrom
    success_url = reverse_lazy('login')
    
    
# class Loginn(LoginView):
#     template_name = 'login.html'
#     form_class =  LoginForm
#     # redirect_authenticated_user = True
#     success_url = reverse_lazy('show_task')


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        
        user = authenticate(username = username, password = password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, 'Loged in successfully')
            return redirect('show_task')
        else:
            messages.error(request, 'User not found')
            return redirect('login')
              
    return render(request, 'login.html')



class LogoutView(View):
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, 'Logged out successfully.')
        return redirect('login')
    

    

