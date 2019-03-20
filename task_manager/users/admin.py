from django.contrib import admin
from django.apps import  AppConfig

# Register your models here.
from .models import Profile,Task,Team

admin.site.register(Profile)
admin.site.register(Task)
admin.site.register(Team)