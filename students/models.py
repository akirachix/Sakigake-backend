from django.db import models
from account.models import Parent
from grade.models import Grade
from phonenumber_field.modelfields import PhoneNumberField


class Student(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    admission_number = models.CharField(max_length=10, unique=True)
    parent_phone_number = PhoneNumberField(region='KE')
    date_added_at = models.DateTimeField(auto_now_add=True)
    date_updated_at= models.DateTimeField(auto_now=True)
    class_grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

   
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

