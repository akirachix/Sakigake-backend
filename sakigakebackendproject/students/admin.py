from django.contrib import admin

from .models import Student

# Register your models here..
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "class_grade", "date_added", "date_updated")
admin.site.register(Student,StudentAdmin)
