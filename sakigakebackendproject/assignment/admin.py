from django.contrib import admin
from .models import Assignment

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('homework', 'resources', 'due_date', 'date_added', 'date_updated')

admin.site.register(Assignment, AssignmentAdmin)

