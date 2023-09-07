from django.contrib import admin
from .models import Parents

class ParentsAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email_address", "phone_number", "student_name", "password", "date_added", "date_updated")
admin.site.register(Parents, ParentsAdmin)