from django.contrib import admin
from .models import School, Teacher, Parent

class TeacherInline(admin.TabularInline):
    model = Teacher

class ParentInline(admin.TabularInline):
    model = Parent

class SchoolAdmin(admin.ModelAdmin):
    inlines = [TeacherInline, ParentInline]
    list_display = ('school_name', 'email_address', 'phonenumber')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email_address', 'school', 'phone_number' )

class ParentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email_address', 'school', 'phone_number')

admin.site.register(School, SchoolAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Parent, ParentAdmin)