import datetime
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Profile(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height >300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Task(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField(blank = True, null = True)
    created_date = models.DateField(default=timezone.now, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    priority = models.IntegerField(default='0')
    creator = models.ForeignKey(
        User, related_name="todo_created_by", on_delete=models.CASCADE
    )
    assignee = models.ForeignKey(
        User,
        blank=True,
        null=True,
        related_name="todo_assigned_to",
        on_delete=models.CASCADE,
    )
    STATUSES = (
        ('Planned ', 'Planned'),
        ('Inprogress', 'Inprogress'),
        ('Done', 'Done'),

    )
    status = models.CharField(max_length=15,null=True, choices=STATUSES, default='Planned')
    #def __init__(self):
     #use   self.status = 'Planned'
    # Has due date for an instance of this object passed?
    def overdue_status(self):
        "Returns whether the Tasks's due date has passed or not."
        if self.due_date and datetime.date.today() > self.due_date:
            return True

    def __str__(self):
        return self.title

    #def get_absolute_url(self):
     #   return reverse("todo:task_detail", kwargs={"task_id": self.id})

    def completed(self):
        if self.status == 'Done' :
            return True

    # Auto-set the Task creation / completed date
    def save(self, **kwargs):
        # If Task is being marked complete, set the completed_date
        if self.completed:
            self.completed_date = datetime.datetime.now()
        super(Task, self).save()
    def get_absolute_url(self):
        return reverse('task-detail',kwargs={'pk':self.pk})
    class Meta:
        ordering = ["priority"]
