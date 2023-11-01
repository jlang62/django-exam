from django.urls import path
from . import views

urlpatterns = [
    path('forms/', views.home_view, name='forms'),
]