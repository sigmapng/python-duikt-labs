from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profiles/', views.profile_list, name='profile_list'),
    path('profiles/<int:blogger_id>/',
         views.profile_detail, name='profile_detail'),
    path('news/', views.news, name='news'),
    path('register/', views.register_blogger, name='register_blogger'),
    path('success/', views.success, name='success'),
    path('login/', views.login_blogger, name='login_blogger'),
]
