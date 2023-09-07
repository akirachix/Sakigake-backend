from django.contrib import admin
from sakigakebackendproject.assignment.models import Assignment

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('teacher,subject,homework,resources')

admin.site.register(Assignment,AssignmentAdmin )

