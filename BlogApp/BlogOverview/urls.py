from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.home_view, name='blogs'),
     path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
]