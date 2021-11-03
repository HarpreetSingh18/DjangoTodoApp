from django.db import models
from django.utils import timezone


# Create your models here.
class TodoItem(models.Model):
    title=models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
     
    def __str__(self):
        return self.title