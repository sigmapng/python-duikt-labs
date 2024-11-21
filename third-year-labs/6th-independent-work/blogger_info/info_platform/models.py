# models.py
from django.db import models

class Blogger(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    social_links = models.JSONField()

    def __str__(self):
        return self.name