from django.contrib.auth.models import User
from django.db import models

# Create your models here.

STATE_CHOICES = (
    ('TODO', 'TODO'),
    ('In Progress', 'In Progress'),
    ('Done', 'Done')
)


class Todo(models.Model):
    task_id = models.CharField(max_length=10,
                               null=True,
                               )
    user = models.ForeignKey(User,
                             related_name='todo',
                             on_delete=models.SET_NULL,
                             null=True,
                             )
    task_title = models.TextField(null=True)
    task_description = models.TextField(null=True)
    task_state = models.CharField(max_length=11,
                                  choices=STATE_CHOICES,
                                  null=True,
                                  )
    task_due_date = models.DateField(null=True)
