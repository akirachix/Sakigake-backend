from django.contrib import admin
from .models import School

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('school_id', 'name', 'email', 'phone_number', 'school_code', 'date_added', 'date_updated')
 
admin.site.register(School, SchoolAdmin)
