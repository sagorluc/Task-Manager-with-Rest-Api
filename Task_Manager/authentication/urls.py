from django.urls import path
from authentication.views import Registration, LogoutView, log_in

urlpatterns = [
    path('', Registration.as_view(), name="register" ),
    path('logout/', LogoutView.as_view(), name="logout" ),
    path('login/', log_in, name="login" ),
    
]
