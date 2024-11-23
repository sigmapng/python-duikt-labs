from django import forms
from django.db import models
from .models import Blogger
from datetime import date


class BloggerRegistrationForm(forms.Form):
    login = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    blog_category = forms.ChoiceField(
        choices=[('tech', 'Tech'), ('lifestyle',
                                    'Lifestyle'), ('food', 'Food')]
    )


class BloggerLoginForm(forms.Form):
    login = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
