from django.db import models


# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=200, blank=False)
    is_complete = models.BooleanField(default=False)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task

