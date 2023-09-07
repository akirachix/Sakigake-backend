from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    teachers = models.ManyToManyField('Teacher', related_name='subjects_taught', blank=True)
    grades = models.JSONField(default=list)

    def __str__(self):
        return self.name