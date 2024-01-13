from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)  # even if we forget to put this in our object, it will
    # automatically give the current time
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title