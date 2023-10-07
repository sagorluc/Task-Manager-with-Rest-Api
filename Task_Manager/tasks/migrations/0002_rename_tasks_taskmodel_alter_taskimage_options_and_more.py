# Generated by Django 4.2.6 on 2023-10-06 11:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tasks',
            new_name='TaskModel',
        ),
        migrations.AlterModelOptions(
            name='taskimage',
            options={'verbose_name': 'Task Image', 'verbose_name_plural': 'Task Images'},
        ),
        migrations.AlterModelOptions(
            name='taskmodel',
            options={'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
    ]