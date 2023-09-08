from django.contrib import admin
from .models import CompetencyBasedGrade  

# class CompetencyBasedGradeAdmin(admin.ModelAdmin):
#     list_display = ('grade_level', 'description')
#     list_filter = ('grade_level',)
#     search_fields = ('grade_level', 'description')
# admin.site.register(CompetencyBasedGrade, CompetencyBasedGradeAdmin)