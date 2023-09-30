from django.contrib import admin

from .models import Student

# Register your models here..
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "class_grade","parent",  "admission_number","date_added_at", "date_updated_at")
admin.site.register(Student,StudentAdmin)
