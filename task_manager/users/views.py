from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    form = UserCreationForm()
    
    return render(request,'users/authenticate/signup.html',{'form':form})
