from django.db import models


class UserData(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # Use a more secure way to store passwords, such as hashing.

    def __str__(self):
        return self.username
