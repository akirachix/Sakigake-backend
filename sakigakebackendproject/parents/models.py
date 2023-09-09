from django.db import models
from students.models import Student
from phonenumber_field.modelfields import PhoneNumberField


class Parent(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email_address = models.EmailField()
    phone_number = models.PhoneNumberField(blank=True, null=True)
    password = models.CharField(max_length=128) 
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    students = models.ManyToManyField(Student)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"