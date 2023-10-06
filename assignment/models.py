from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from subject.models import Subject
from shop.models import Shop

class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, editable=True)
    topic = models.CharField(max_length=50)
    competency = models.CharField(max_length=100)
    task = models.TextField()
    resources = ArrayField(models.CharField(max_length=50))
    category = models.ForeignKey(Shop, on_delete=models.CASCADE)
    due_date = models.DateTimeField(default=timezone.now)
    date_added_at = models.DateTimeField(default=timezone.now)
    date_updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.topic
    