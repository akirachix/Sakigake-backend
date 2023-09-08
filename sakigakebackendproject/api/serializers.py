from rest_framework import serializers

from assignment.models import Assignment
from notification.models import Notification

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = "_all_"

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "_all"

