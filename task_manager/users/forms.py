from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Task,Team

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
    description = forms.CharField(widget=forms.Textarea,required=False)
    priority = forms.IntegerField(max_value=10)
    due_date = forms.DateField()

    assignee = forms.ChoiceField(choices=User.objects.all())
    STATUSES = (
        ('Planned ', 'Planned'),
        ('Inprogress', 'Inprogress'),
        ('Done', 'Done'),

    )


    status =forms.ChoiceField(choices=STATUSES)
    #def get_my_choices():

     #   return choices_list

    #def __init__(self, *args, **kwargs):
     #   super(TaskCreationForm, self).__init__(*args, **kwargs)
      #  self.fields['assignee'] = forms.ChoiceField(
       # choices=get_my_choices())

    class Meta:
        model = Task
        fields = ('title','description','assignee','priority','due_date','status')




class TeamCreationForm(forms.ModelForm):
    TeamName = forms.CharField(max_length=26,required=True)
    TeamMember = forms.ModelChoiceField(queryset=User.objects.all())
    class Meta:
        model = Team
        fields = ('TeamName','TeamMember')

