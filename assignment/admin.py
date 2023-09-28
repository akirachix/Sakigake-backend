from django.contrib import admin
from .models import Assignment

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('subject','topic','task','competency', 'resources', 'category','due_date',
                    'date_added_at','date_updated_at')

admin.site.register(Assignment, AssignmentAdmin)

