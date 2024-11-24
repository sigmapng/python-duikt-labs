# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Blogger
import random
from .forms import BloggerRegistrationForm, BloggerLoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password, make_password


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
            blogger = form.save(commit=False)
            blogger.password = make_password(form.cleaned_data['password'])
            blogger.save()
            return redirect('registration_success')
    else:
        form = BloggerRegistrationForm()
    return render(request, 'register_blogger.html', {'form': form})


def login_blogger(request):
    if request.method == 'POST':
        form = BloggerLoginForm(request.POST)
        if form.is_valid():
            login_input = form.cleaned_data['login']
            password_input = form.cleaned_data['password']
            try:
                blogger = Blogger.objects.get(login=login_input)
                if check_password(password_input, blogger.password):
                    request.session['blogger_id'] = blogger.id
                    request.session['login_success'] = True
                    return redirect('login_success')
                else:
                    form.add_error(None, 'Invalid login or password')
            except Blogger.DoesNotExist:
                form.add_error(None, 'Invalid login or password')
    else:
        form = BloggerLoginForm()
    return render(request, 'login_blogger.html', {'form': form})


def registration_success(request):
    return render(request, 'registration_success.html')


def login_success(request):
    return render(request, 'login_success.html')
