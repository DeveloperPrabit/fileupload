# pages/admin.py
from django.contrib import admin
from .models import Page, File

from .models import ContactInfo
from .models import AboutUs
from .models import TermsAndConditions, PrivacyPolicy

admin.site.register(TermsAndConditions)
admin.site.register(PrivacyPolicy)

admin.site.register(AboutUs)

admin.site.register(ContactInfo)

class FileInline(admin.TabularInline):
    model = File
    extra = 1

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [FileInline]

admin.site.register(Page, PageAdmin)
