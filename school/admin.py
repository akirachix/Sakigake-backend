from django.contrib import admin
from .models import School

class SchoolAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'email' ,'grades','phone_number','school_code', 'date_added_at', 'date_updated_at')
 
admin.site.register(School, SchoolAdmin)