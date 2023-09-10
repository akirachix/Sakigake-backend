from django.contrib import admin

from .models import Parent

# Register your models here..
class ParentAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name", "email_address", "date_added_at", "date_updated_at")
admin.site.register(Parent, ParentAdmin)
