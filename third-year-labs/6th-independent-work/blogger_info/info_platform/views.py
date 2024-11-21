from django.shortcuts import render, redirect
from .models import bloggers


def home(request):
    return render(request, 'home.html')


def profiles(request):
    return render(request, 'profiles.html', {'bloggers': bloggers})


def profile_detail(request, name):
    blogger = next((b for b in bloggers if b.name == name), None)
    if blogger:
        return render(request, 'profile_detail.html', {'blogger': blogger})
    else:
        return render(request, '404.html', status=404)


def news(request):
    return redirect('home')
