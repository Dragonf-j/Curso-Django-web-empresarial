from django.shortcuts import render, get_object_or_404
from .models import Page
# Create your views here.

def page(request, pages_id):
    pages = get_object_or_404(Page,id=pages_id)
    return render(request, 'pages/sample.html', {'page':pages})