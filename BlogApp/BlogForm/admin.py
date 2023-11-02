from django.contrib import admin
from .models import BlogModel

# Register your models here.

class Blogs(admin.ModelAdmin):
    list_display = ("title", "author", "created_on")

admin.site.register(BlogModel, Blogs)

