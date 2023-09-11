from django.contrib import admin
from .models import Subject

class SubjectAdmin(admin.ModelAdmin):
    list_display = ("subject_name", "description")

admin.site.register(Subject, SubjectAdmin)