from django.db import models
from parents.models import Parent
from phonenumbers import PhoneNumberField


class Student(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    parent_phone_number = models.PhoneNumberField(blank=True, null=True)
    date_added_at = models.DateTimeField(auto_now_add=True)
    date_updated_at= models.DateTimeField(auto_now=True)
    class_grade = models.CharField(max_length=32)
    parent = models.ForeignKey(Parent, null=True, on_delete=models.CASCADE)

   
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    