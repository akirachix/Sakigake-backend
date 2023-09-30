from django.contrib import admin
from .models import School, Teacher, Parent

class TeacherInline(admin.TabularInline):
    model = Teacher

class ParentInline(admin.TabularInline):
    model = Parent

class SchoolAdmin(admin.ModelAdmin):
    inlines = [TeacherInline, ParentInline]
    list_display = ('school_name', 'email_address', 'phonenumber','create_password','confirm_password')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','is_class_teacher', 'email_address', 'school', 'phone_number','create_password','confirm_password' )

class ParentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email_address', 'school', 'phone_number','create_password','confirm_password')


admin.site.register(School, SchoolAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Parent, ParentAdmin)