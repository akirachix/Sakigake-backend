from django.contrib import admin
from .models import Teacher

class TeachersAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone_number","email","password", "is_class_teacher", "date_added_at", "date_updated_at")

admin.site.register(Teacher, TeachersAdmin)