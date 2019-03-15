from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Group(models.model):
    TeamLead = models.ForeignKey(
        User, related_name="Team leader", on_delete=models.CASCADE
    )
    TeamName = models.CharField(max_length=25)

    def __str__(self):
        return self.TeamName


class TeamMember(models.Model):
    MemberName = models.ForeignKey(
        User, related_name="Team Member", on_delete=models.CASCADE
    )
    TeamName = models.ForeignKey(
        Group, related_name="todo_created_by", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.TeamName

