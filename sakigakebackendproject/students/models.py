from django.db import models
from parents.models import Parent
from phonenumber_field.modelfields import PhoneNumberField


class Student(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    admission_number = models.CharField(max_length=10, unique=True, default="")
    parent_phone_number = PhoneNumberField(region='KE')
    date_added_at = models.DateTimeField(auto_now_add=True)
    date_updated_at= models.DateTimeField(auto_now=True)
    class_grade = models.CharField(max_length=32)
    parent = models.ForeignKey(Parent, null=True, on_delete=models.CASCADE)

   
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    