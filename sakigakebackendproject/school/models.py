import random
import string
import phonenumbers
from django.core.exceptions import ValidationError
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

def validate_phone_number(value):
    try:
        parsed_number = phonenumbers.parse(value, None)
        if not phonenumbers.is_valid_number(parsed_number):
            raise ValidationError("Invalid phone number")
    except phonenumbers.phonenumberutil.NumberFormatException:
        raise ValidationError("Invalid phone number format")

class School(models.Model):
    school_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True, null=True, validators=[validate_phone_number])
    website = models.URLField()
    location = models.CharField(max_length=200)
    subjects = models.CharField(max_length=200)  
    school_code = models.CharField(max_length=20, unique=True, blank=True, null=True)
    date_added_at = models.DateTimeField(auto_now_add=True, verbose_name="Date Added")
    date_updated_at = models.DateTimeField(auto_now=True, verbose_name="Date Updated")

    def generate_school_code(self):
      
        code_length = 8 
        characters = string.ascii_uppercase + string.digits
        code = ''.join(random.choice(characters) for _ in range(code_length))
        return code

    def save(self, *args, **kwargs):
        if not self.school_code:
            self.school_code = self.generate_school_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
