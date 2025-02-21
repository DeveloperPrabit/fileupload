# pages/views.py
from django.shortcuts import render, get_object_or_404
from .models import Page

def home(request):
    return render(request, 'pages/home.html')

def contact(request):
    return render(request, 'pages/contact.html')

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'pages/page_detail.html', {'page': page})
