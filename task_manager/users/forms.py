from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Task

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length= 30,required = False,help_text='Optional')
    last_name = forms.CharField(max_length= 30,required=False, help_text='Optional' )
    email = forms.EmailField(max_length = 254,help_text='Required.Inform a valid email address')
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class TaskCreationForm(forms.ModelForm):
    title = forms.CharField(max_length=140,required=True)
    description = forms.TextField(blank=True, null=True)
    priority = forms.IntegerField(default='0',max_value=10)
    #assignee
    class Meta:
        model = Task
        fields = ('title','descritpion','priority')
