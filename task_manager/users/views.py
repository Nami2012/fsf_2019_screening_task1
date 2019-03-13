from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from .forms import SignUpForm,UserUpdateForm,ProfileUpdateForm,TaskCreationForm
from .models import Task
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
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance = request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance= request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated')
            return  redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'users/authenticate/profile.html',context)

def firstpage(request):
    return render(request,"base.html")


def task(request):
    context = {
        'tasks':Task.objects.all()
    }

    #return render(request,'users/tasks.html',context)

class TaskListView(ListView):
    model = Task
    template_name = 'users/tasks.html'
    context_object_name = 'tasks'
#    ordering = ['date_posted']


class TaskDetailView(DetailView):
    model = Task

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'priority', 'assignee','due_date','status']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)