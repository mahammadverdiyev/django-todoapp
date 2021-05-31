from django.db import models


class Todo(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
