"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
#from TeamTasks import views as Team_tasks_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',user_views.home),
    path('signup/',user_views.signup, name='signup'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/authenticate/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/authenticate/logout.html'), name='logout'),
    path('home/', user_views.home, name='home'),
    path('tasks/',user_views.TaskListView.as_view(),name = 'task'),
    path('tasks/<int:pk>/', user_views.TaskDetailView.as_view(), name='task-detail'),
    path('tasks/new/', user_views.TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/update', user_views.TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete', user_views.TaskDeleteView.as_view(), name='task-delete'),
    path('team/create/',user_views.TeamCreateView.as_view(),name = 'new'),
    path('team/list/',user_views.TeamListView,name = 'team'),
    path('team/<int:pk>/details',user_views.TeamDetailView,name = 'team-details'),
    path('team/<int:pk>/update', user_views.TeamUpdateView.as_view(), name='team-update'),
    path('team/<int:pk>/delete', user_views.TeamDeleteView.as_view(), name='team-delete'),
    path('team/tasks/<int:pk>/new/', user_views.TeamTaskCreateView, name='team-task-create'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
