from django import forms
from .models import BlogModel

class InputForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['title', 'author', 'content', 'img', 'video']