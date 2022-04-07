from django.contrib.auth.models import User
from django.db import models

# Create your models here.

STATE_CHOICES = (
    ('TODO', 'TODO'),
    ('In Progress', 'In Progress'),
    ('Done', 'Done')
)


class Todo(models.Model):
    task_id = models.CharField(max_length=10)
    user = models.ForeignKey(User,
                             related_name='todo',
                             on_delete=models.SET_NULL,
                             null=True,
                             )
    task_title = models.TextField()
    task_description = models.TextField()
    task_state = models.CharField(max_length=11,
                                  choices=STATE_CHOICES,
                                  )
    task_due_date = models.DateField()
