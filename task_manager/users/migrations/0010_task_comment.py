# Generated by Django 2.1.7 on 2019-03-30 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_task_teamname'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='comment',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
