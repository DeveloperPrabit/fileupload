# pages/views.py
from django.shortcuts import render, get_object_or_404
from .models import Page
from .models import ContactInfo
from .models import AboutUs  # Import the model that holds About Us content

def about(request):
    about_data = AboutUs.objects.first()  # Fetch first entry or modify logic if needed
    return render(request, "pages/about.html", {"about": about_data})


def contact_view(request):
    contact = ContactInfo.objects.first()  # Get the first contact info
    return render(request, 'pages/contact.html', {'contact': contact})


def home(request):
    return render(request, 'pages/home.html')

# def contact(request):
#     return render(request, 'pages/contact.html')

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'pages/page_detail.html', {'page': page})
