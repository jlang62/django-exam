from django.shortcuts import render
from .forms import InputForm
from .models import BlogModel
import logging

logger = logging.getLogger(__name__)

def home_view(request):
    context = {}

    if request.method == 'POST':
        form = InputForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            logger.info("Form saved successfully.")
        else:
            logger.error("Form is not valid. Errors: %s", form.errors)

    items = BlogModel.objects.all()
    context['form'] = InputForm()
    context['items'] = items

    return render(request, "form.html", context)
