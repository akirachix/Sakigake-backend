from django.db import models

from firebase_admin import messaging

# Create your models here.
class Assignment(models.Model):
    # sender = models.ForeignKey(Teacher,on_delete=models.CASCADE, editable=True)
    # recipient = models.ForeignKey(Parent, on_delete=models.CASCADE, editable=True)
    # subject = models.ForeignKey(Subject, on_delete=models.CASCADE, editable=True)
    topic = models.CharField(max_length=54,null=True)
    competency = models.CharField(max_length=64)
    task = models.TextField()
    materials = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    due_date = models.DateTimeField()
    date_added_at = models.DateTimeField()
    date_updated_at = models.DateTimeField()

    

    def send_push_notification(self):
        message = messaging.Message(
            notification = message.Notification(
                title ="New Assignment",
                body = {self.topic},
            ),
            topic = "assignments"
        )
        response = messaging.send(message)
        print("Successfully sent notification:", response)
    def save(self):
        super().save
        self.send_push_notification()

    def __str__(self):
        return self.topic

