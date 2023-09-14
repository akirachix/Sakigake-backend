from django.contrib import admin
from .models import CustomUser, Teacher 

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email','school_name','email',)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'created_by')



admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Teacher, TeacherAdmin)
# admin.site.register(Parent, ParentAdmin)