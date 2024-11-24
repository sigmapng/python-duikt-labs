from django import forms
from .models import Blogger


class BloggerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Blogger
        fields = ['login', 'password', 'name', 'description', 'category']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'login': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Login'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }


class BloggerLoginForm(forms.Form):
    login = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Login'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
