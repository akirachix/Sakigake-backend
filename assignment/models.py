from django.db import models
from django.contrib.postgres.fields import ArrayField
from subject.models import Subject
from shop.models import Shop

class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, editable=True)
    topic = ArrayField(models.CharField(max_length=50), default=list)
    competency = models.CharField(max_length=100)
    task = models.TextField()
    resources = ArrayField(models.CharField(max_length=50), default=list)
    category = models.ForeignKey(Shop, on_delete=models.CASCADE)
    due_date = models.DateTimeField(default=None, null=True, blank=True)
    date_added_at = models.DateTimeField(default=None, null=True, blank=True)
    date_updated_at = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return self.topic