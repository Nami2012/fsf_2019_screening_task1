from django.urls import path
from .views import LoginView,signup,logout
app_name = 'tm'
urlpatterns = [
    path('login',LoginView,name = 'login'),
    path('signup', signup, name='signup'),
    path('logout',logout,name = 'logout')

]
