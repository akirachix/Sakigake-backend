from django.contrib import admin
from .models import Teacher

class TeachersAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email","password", "is_class_teacher", "date_added", "date_updated")

admin.site.register(Teacher, TeachersAdmin)