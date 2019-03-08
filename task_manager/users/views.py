from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
            form = SignUpForm(request.POST)

            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request,f'Your account has been created')
                return redirect('login')
    else:
        form = SignUpForm()


    return render(request,'users/authenticate/signup.html',{'form':form})
def home(request):
    return HttpResponse('you are logged in')

@login_required
def profile(request):
    return render(request,'users/authenticate/profile.html')

def firstpage(request):
    return render(request,"base.html")
