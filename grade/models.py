from django.db import models
from teachers.models import Teacher
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator
from multiselectfield.validators import MaxValueMultiFieldValidator


class Grade(models.Model):
    SUBJECT_CHOICES = (
        ('1', 'Math'),
        ('2', 'English'),
        ('3', 'Kiswahili'),
        ('4', 'Science'),
        ('5', 'Agriculture'),
        ('6', 'Art & Design'),
    )
    
    grade_name = models.CharField(max_length=50)
    class_teacher = models.OneToOneField(Teacher, on_delete=models.SET_NULL, null=True, related_name='grade')
    subjects = MultiSelectField(choices=SUBJECT_CHOICES, validators=[MaxValueMultiFieldValidator(6)]) 