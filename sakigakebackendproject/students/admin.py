from django.contrib import admin
from .models import Students

# Register your models here.
class StudentsAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "admission_id", "date_added", "date_updated")
admin.site.register(Students, StudentsAdmin)