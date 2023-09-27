from django.contrib import admin
from .models import Grade

class GradeAdmin(admin.ModelAdmin):
    list_display = ("grade_name", "class_teacher", "subjects")
admin.site.register(Grade, GradeAdmin)

# Register your models here..