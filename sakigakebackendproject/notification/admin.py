from django.contrib import admin

from django.contrib import admin
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('preview', 'timestamp',)

admin.site.register(Notification, NotificationAdmin)
