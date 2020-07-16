from django.contrib import admin
from app_name.models import ContactForm

class ContactFormkAdmin(admin.ModelAdmin):
    search_fields = ["pk","full_name"]
    list_filter = ["full_name"]
    list_display = [
        "pk",
        'created_at',
        "full_name",
        "email_id",
        "contact_number",
        "message",
    ]
    list_editable = ["full_name"]
 

admin.site.register(ContactForm,ContactFormkAdmin)
