from django.urls import path
from . import views

urlspartterns = [
    path('', views.post_list, name='post_list'),
]