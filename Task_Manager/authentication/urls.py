from django.urls import path
from authentication.views import Registration, LogoutView, log_in, change_password, forget_password

urlpatterns = [
    path('', Registration.as_view(), name="register" ),
    path('logout/', LogoutView.as_view(), name="logout" ),
    path('login/', log_in, name="login" ),
    path('foget_pass/', forget_password, name='forget_pass'),
    path('change_pass/<token>/', change_password, name='change_pass'),
   
    
]
