from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Generate the forget password token

class GeneratePasswordToken(models.Model):
     user_pass             = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_pass')
     forget_password_token = models.CharField(max_length= 200)
     created_at            = models.DateTimeField(auto_now_add=True)
     
     def __str__(self) -> str:
          return self.user_pass.username

