
from django.core.mail import send_mail
from django.conf import settings
import uuid # this will generate the token

def send_forget_password_mail(email, token):
    subject = 'Your Forget Password Link : '
    message = f'Hi ! Click the link to reset your password : http://127.0.0.1:8000/auth/change_pass/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True
