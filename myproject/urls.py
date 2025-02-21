from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .forms import PasswordResetFormWithCaptcha
from django.contrib.auth.views import LoginView
from .forms import AdminLoginForm
urlpatterns = [
    # Admin login URL
    path("admin/login/", LoginView.as_view(authentication_form=AdminLoginForm), name='admin_login'),
    
    # Admin panel URL
    path('admin/', admin.site.urls),
    
    # Password reset URLs
    path('password_reset/', PasswordResetView.as_view(
    form_class=PasswordResetFormWithCaptcha,
    email_template_name="registration/password_reset_email.html",
    extra_context={'site_name': 'TechProgramming'}
), name='password_reset'),


    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    # Include pages URLs
    path('', include('pages.urls')),  # Include your app's URLs
]


# Serve media files in development (when DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)