from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import SignUpForm,UserUpdateForm,ProfileUpdateForm,TaskCreationForm
from .models import Task,Team
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

class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'users/tasks.html'
    context_object_name = 'tasks'
#    ordering = ['date_posted']


class TaskDetailView(DetailView):
    model = Task

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'priority','due_date','status']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Task
    fields = ['title', 'description', 'priority','due_date','status']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    def test_func(self):
        task = self.get_object()
        if self.request.user == task.creator:
            return True
        return False

class TaskDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Task
    fields = ['title', 'description', 'priority','due_date','status']
    success_url = '/tasks'
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    def test_func(self):
        task = self.get_object()
        if self.request.user == task.creator:
           return True
        return False

#class TeamListView(ListView):
 #   model = Team
  #  template_name = 'TeamTasks/team_list.html'
   # context_object_name = 'team'
#    ordering = ['date_posted']

def TeamListView(request):
    team = Team.objects.get(id=1)
    Members = team.MemberName.all()
    context = {
        'team_Name': team.TeamLead,
        'team_Lead': team.TeamName,
        'Members':Members

    }
    return render(request, "TeamTasks/team_list.html", context)


class TeamCreateView(CreateView):
    model = Team
    fields = ['TeamName', 'MemberName']
    template_name = 'TeamTasks/team_form.html'
    def form_valid(self, form):
        form.instance.TeamLead = self.request.user
        return super().form_valid(form)