from django.contrib import admin
from django.apps import  AppConfig

# Register your models here.
from .models import Profile

admin.site.register(Profile)