from django.db import models
from teachers.models import Teacher
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator
from multiselectfield.validators import MaxValueMultiFieldValidator


class Grade(models.Model):
   
    grade_name = models.CharField(max_length=50)
    class_teacher = models.OneToOneField(Teacher, on_delete=models.SET_NULL,null=True, related_name='grade')