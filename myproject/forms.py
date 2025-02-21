from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django_recaptcha.fields import ReCaptchaField
from django.contrib.auth.forms import PasswordResetForm

class PasswordResetFormWithCaptcha(PasswordResetForm):
    captcha = ReCaptchaField()  # Adds a CAPTCHA field for password reset form


class AdminLoginForm(AuthenticationForm):
    captcha = ReCaptchaField()  # Adds a CAPTCHA field for admin login form
