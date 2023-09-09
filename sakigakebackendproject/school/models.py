from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class School(models.Model):
    school_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True, null=True)
    website = models.URLField()
    location = models.CharField(max_length=200)
    subjects = models.CharField(max_length=200)  
    school_code = models.CharField(max_length=20, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name