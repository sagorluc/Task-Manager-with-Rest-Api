# Generated by Django 4.2.6 on 2023-11-08 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneratePasswordToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forget_password_token', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_pass', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_pass', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
