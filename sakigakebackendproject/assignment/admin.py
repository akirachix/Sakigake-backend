from django.contrib import admin
from .models import Assignment

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('topic','task','competency', 'materials', 'category','due_date')

admin.site.register(Assignment, AssignmentAdmin)

