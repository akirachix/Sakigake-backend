from django.db import models
from .models import Teacher

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    teachers = models.ManyToManyField('Teacher', related_name='subjects_taught', blank=True)
    grades = models.ManyToManyField('Grade')

    def __str__(self):
        return self.name