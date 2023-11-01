from django.shortcuts import render
from django.http import HttpResponse
from BlogForm.models import BlogModel

# Create your views here.
def home_view(request):
    context = {}
    items = BlogModel.objects.all()
    context['items'] = items

    return render(request, "blogs.html", context)