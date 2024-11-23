from django.db import models


class Blogger(models.Model):
    login = models.CharField(max_length=100, default='default_login')
    password = models.CharField(max_length=100, default='default_password')
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
