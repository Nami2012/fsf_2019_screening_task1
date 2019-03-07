from django.urls import path
from .views import signup,home
app_name = 'tm'
urlpatterns = [

    path('signup', signup, name='signup'),


]
