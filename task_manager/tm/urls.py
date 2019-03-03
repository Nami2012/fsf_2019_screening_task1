from django.urls import path
from .views import LoginView
app_name = 'tm'
urlpatterns = [
    path('',LoginView)
]