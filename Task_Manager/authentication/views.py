from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from authentication.forms import RegistrationFrom, LoginForm
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from .email_helpers import send_forget_password_mail
from .models import GeneratePasswordToken
from django.views.decorators.csrf import csrf_exempt
import uuid


# PasswordChangeForm need old password
# SetPasswordForm no need old password
# update_session_auth_hash we can see the password

# Create your views here.
class Registration(CreateView):
    model         = User
    template_name = 'register.html'
    form_class    = RegistrationFrom
    success_url   = reverse_lazy('login')
    
    
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
    
  
  
#============================ change the forgot password ============================    
@csrf_exempt   
def change_password(request, token):
    
    context = {}
    try:
        profile_obj = GeneratePasswordToken.objects.filter(forget_password_token= token).first() # token
        print(profile_obj)
        
        context = {'user_id' : profile_obj.user_pass.id} # ekhane ektu jamela ace. id not getting
        
        if request.method == "POST":
            new_password     = request.POST.get('new-password')
            confirm_password = request.POST.get('confirm-password')
            user_id = request.POST.get('user_id')
            print(user_id)
            
            if user_id is None:
                messages.success(request, 'User id is none or Not found')
                return redirect(f'change_pass/{token}')
            
           
            if new_password != confirm_password:
                messages.success(request, "Password does not match")
                return redirect(f'change_pass/{token}')
            
        
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            messages.success(request, "Password has been change successfully.")
            return redirect('login')
        
    except Exception as e:
        print(e)
    
    return render(request, 'change_pass.html', context)





#============================== Check by Username =============================  
@csrf_exempt   
def forget_password(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username') # get the username from input form
            # print(username)
                       
            if not User.objects.filter(username=username).first(): # filter username
                messages.success(request, "This user is not found! ")
                return redirect('forget_pass')
            else:
                user_obj  = User.objects.get(username= username) # get username
                
                token     = str(uuid.uuid4()) # generate token
                user_prof = GeneratePasswordToken(user_pass = user_obj) # username of user_profile
                user_prof.forget_password_token = token # user token
                user_prof.save()
                
                send_forget_password_mail(user_obj.email, token)
                messages.success(request, "An email is sended to you email")
                return redirect('forget_pass')
                   
    except Exception as e:
        print(e)
        
    return render(request, 'forget_pass.html')
    



            

