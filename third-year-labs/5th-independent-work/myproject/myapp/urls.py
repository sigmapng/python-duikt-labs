from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_info_view, name='my_info'),
]
