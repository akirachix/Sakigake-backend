from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# from school.models import School

class Parent(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email_address = models.EmailField(null=True)
    # school = models.ManyToManyField(School)
    phone_number = PhoneNumberField(unique=True, region='KE')
    date_added_at = models.DateTimeField(auto_now_add=True)
    date_updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"