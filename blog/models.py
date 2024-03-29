from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)  # even if we forget to put this in our object, it will
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.first_name