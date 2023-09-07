from django.contrib import admin

from sakigakebackendproject.notification.models import Notification

# Register your models here.
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('teacher,parent, subject, timestamp')

admin.site.register(Notification,NotificationAdmin )