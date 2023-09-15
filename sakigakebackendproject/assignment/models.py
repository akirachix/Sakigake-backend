from django.db import models
from django.contrib.postgres.fields import ArrayField
from firebase_admin import messaging
import requests
from subject.models import Subject
from shop.models import Shop


# Create your models here.
class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, editable=True)
    topic = models.CharField(max_length=54,null=True)
    competency = models.CharField(max_length=100)
    task = models.TextField()
    materials = ArrayField(models.CharField(max_length=50))
    category = models.ForeignKey(Shop, on_delete=models.CASCADE)
    due_date = models.DateTimeField(default=None, null=True, blank=True)
    date_added_at = models.DateTimeField(default=None, null=True, blank=True)
    date_updated_at = models.DateTimeField(default=None, null=True, blank=True)

def __str__(self):
        return self.topic

