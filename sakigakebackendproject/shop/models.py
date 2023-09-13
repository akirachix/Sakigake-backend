from django.db import models

from assignment.models import Assignment
from phonenumber_field.modelfields import PhoneNumberField


class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=60)
    phone_number = PhoneNumberField(null=True)
    category = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name