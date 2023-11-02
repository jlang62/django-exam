from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from BlogForm.models import BlogModel

# Create your views here.
def home_view(request):
    context = {}
    items = BlogModel.objects.all()
    context['items'] = items

    return render(request, "blogs.html", context)

def blog_detail(request, blog_id):
    blog = get_object_or_404(BlogModel, id=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})