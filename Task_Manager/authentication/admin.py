from django.contrib import admin
from .models import GeneratePasswordToken

# Register your models here.

class GeneratePasswordTokenAdmin(admin.ModelAdmin):
    list_display = ['forget_password_token']
    ordering = ['id']


admin.site.register(GeneratePasswordToken, GeneratePasswordTokenAdmin)