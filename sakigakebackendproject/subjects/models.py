from django.db import models
# from .models import Teacher
# from .models import Grade


class Subject(models.Model):
    CHOICES = (
        ('1', 'English'),
        ('2', 'Kiswahili'),
        ('3', 'Mathematics'),
        ('4', 'Integrated Science'),
        ('5', 'Social Studies'),
        ('6', 'Business Studies'),
        ('7', 'Agriculture'),
        ('8', 'Pre-technical and Pre-Career Studies'),
        ('9', 'Religious Studies Education'),
    )
    subject_name = models.CharField(max_length=100, choices=CHOICES)
    description = models.TextField(blank=True)
    # teachers = models.ManyToManyField('Teacher', related_name='subjects_taught', blank=True)
    # grades = models.ManyToManyField('Grade')

    def __str__(self):
        return self.subject_name
    
