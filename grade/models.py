from django.db import models
from account.models import Teacher
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator
from multiselectfield.validators import MaxValueMultiFieldValidator


class Grade(models.Model):
    grade_name = models.CharField(max_length=50)
    class_teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)