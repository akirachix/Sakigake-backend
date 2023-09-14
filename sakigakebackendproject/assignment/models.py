from django.db import models
from django.contrib.postgres.fields import ArrayField
from firebase_admin import messaging

from shop.models import Shop



# Create your models here.
class Assignment(models.Model):
    # sender = models.ForeignKey(Teacher,on_delete=models.CASCADE, editable=True)
    # recipient = models.ForeignKey(Parent, on_delete=models.CASCADE, editable=True)
    # subject = models.ForeignKey(Subject, on_delete=models.CASCADE, editable=True)
    topic = models.CharField(max_length=54,null=True)
    competency = models.CharField(max_length=100)
    task = models.TextField()
    materials = ArrayField(models.CharField(max_length=50))
    category = models.ForeignKey(Shop, on_delete=models.CASCADE)
    due_date = models.DateTimeField(default=None, null=True, blank=True)
    date_added_at = models.DateTimeField(default=None, null=True, blank=True)
    date_updated_at = models.DateTimeField(default=None, null=True, blank=True)

    def send_push_notification(self):
        message = messaging.Message(
            notification = message.Notification(
                title = {self.topic},
                body = {self.task},
            ),
            topic = "assignments"
        )
        response = messaging.send(message)
        print("Successfully sent notification:", response)
    def save(self):
     super().save()
     self.send_push_notification()


    def __str__(self):
        return self.topic

