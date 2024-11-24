# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Blogger
import random
from .forms import BloggerRegistrationForm, BloggerLoginForm
from django.contrib.auth import authenticate, login


def index(request):
    bloggers = Blogger.objects.all()
    random_blogger = random.choice(bloggers) if bloggers else None
    top_bloggers = bloggers[:5]
    return render(request, 'index.html', {'random_blogger': random_blogger, 'top_bloggers': top_bloggers})


def profile_list(request):
    bloggers = Blogger.objects.all()
    return render(request, 'profile_list.html', {'bloggers': bloggers})


def profile_detail(request, blogger_id):
    blogger = get_object_or_404(Blogger, id=blogger_id)
    return render(request, 'profile_detail.html', {'blogger': blogger})


def news(request):
    return render(request, 'news.html')


def success(request):
    return render(request, 'success.html')


def register_blogger(request):
    if request.method == 'POST':
        form = BloggerRegistrationForm(request.POST)
        if form.is_valid():
            Blogger.objects.create(
                login=form.cleaned_data['login'],
                password=form.cleaned_data['password'],
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['blog_category'],
            )
            return redirect('success')
    else:
        form = BloggerRegistrationForm()
    return render(request, 'register_blogger.html', {'form': form})


def login_blogger(request):
    if request.method == 'POST':
        form = BloggerLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile_list')
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = BloggerLoginForm()
    return render(request, 'login_blogger.html', {'form': form})
