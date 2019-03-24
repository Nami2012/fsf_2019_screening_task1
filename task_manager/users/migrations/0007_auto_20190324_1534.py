# Generated by Django 2.1.7 on 2019-03-24 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190324_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assignee',
            field=models.ForeignKey(blank=True, default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo_created_by', to=settings.AUTH_USER_MODEL), null=True, on_delete=django.db.models.deletion.CASCADE, related_name='todo_assigned_to', to='users.Team'),
        ),
    ]
