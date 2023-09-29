from django.db import models
from account.models import Teacher

class Subject(models.Model):
    subject_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return self.subject_name