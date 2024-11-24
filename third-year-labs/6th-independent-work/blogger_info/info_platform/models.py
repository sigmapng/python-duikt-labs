from django.db import models


class Blogger(models.Model):
    login = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=[
        ('gaming', 'Gaming'), ('lifestyle', 'Lifestyle'),
        ('food', 'Food'), ('travel', 'Travel')
    ])

    def __str__(self):
        return self.name
