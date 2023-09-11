import random
import string
import phonenumbers
from django.core.exceptions import ValidationError
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone 

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
    subjects = models.CharField(max_length=50 , default='')
    phone_number = PhoneNumberField(blank=True, null=True, validators=[validate_phone_number])
    website = models.URLField()
    location = models.CharField(max_length=200)
    school_code = models.CharField(max_length=20, unique=True, blank=True, null=True)
    date_added_at = models.DateTimeField(default=timezone.now, verbose_name="Date Added")
    date_updated_at = models.DateTimeField(auto_now=True, verbose_name="Date Updated")

    
    def generate_school_code(self):
     
        cleaned_name = self.name.replace(" ", "").capitalize()

        if len(cleaned_name) < 4:
            pad_length = 4 - len(cleaned_name)
            padding = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(pad_length))
            code = cleaned_name + padding
        else:
            code = cleaned_name[:4]

        code += ''.join(random.choice(string.digits) for _ in range(4))

        return code

    def save(self, *args, **kwargs):
        if not self.school_code:
            self.school_code = self.generate_school_code()
        super().save(*args, **kwargs)

