from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.home_view, name='blogs'),
]