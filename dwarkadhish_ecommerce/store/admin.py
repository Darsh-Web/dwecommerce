from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'submitted_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('submitted_at',)

from .models import OEMInquiry

@admin.register(OEMInquiry)
class OEMInquiryAdmin(admin.ModelAdmin):
    list_display = ("company_name", "contact_name", "email", "phone", "gem_registered", "submitted_at")
    search_fields = ("company_name", "contact_name", "email")
    list_filter = ("gem_registered", "submitted_at")