from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profiles/', views.profiles, name='profiles'),
    re_path(r'^profiles/(?P<name>[\w\s]+)/$',
            views.profile_detail, name='profile_detail'),
    path('news/', views.news, name='news'),
]
