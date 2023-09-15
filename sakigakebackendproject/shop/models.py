from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=60)
    phone_number = PhoneNumberField(null=True)
    category = models.CharField()
    
    def __str__(self):
        return self.category
    
    