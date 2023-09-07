from django.contrib import admin
from .models import Subject

class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "teachers", "grades")

admin.site.register(Subject, SubjectAdmin)