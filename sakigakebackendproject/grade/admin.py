from django.contrib import admin
from .models import CompetencyBasedGrade

class CompetencyBasedGradeAdmin(admin.ModelAdmin):
    list_display = ('description', 'grade')
    list_filter = ('grade', 'subjects', 'teachers', 'assignments')
    search_fields = ('description', 'grade', 'subjects__name', 'teachers__name', 'assignments__title')
admin.site.register(CompetencyBasedGrade,CompetencyBasedGradeAdmin)