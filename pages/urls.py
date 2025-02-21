# pages/urls.py
from django.urls import path
from .views import home, contact, page_detail

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),  # Update to use contact view
    path('<slug:slug>/', page_detail, name='page_detail'),
]
