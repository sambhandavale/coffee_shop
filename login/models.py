from django.db import models


class UserData(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=254,default='default@example.com')

    def __str__(self):
        return self.username
