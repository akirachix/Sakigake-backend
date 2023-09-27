import random
import string
from django.core.exceptions import ValidationError
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.core.validators import validate_email
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator
from multiselectfield.validators import MaxValueMultiFieldValidator



class School(models.Model):
    GRADE_CHOICES = (
        ('1', 'Grade 1'),
        ('2', 'Grade 2'),
        ('3', 'Grade 3'),
        ('4', 'Grade 4'),
        ('5', 'Grade 5'),
        ('6', 'Grade 6'),
    ) 

    school= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(validators=[validate_email])
    grades = MultiSelectField(choices=GRADE_CHOICES, validators=[MaxValueMultiFieldValidator(6)]) 
    phone_number = PhoneNumberField(blank=True, null=True)
    website = models.URLField()
    location = models.CharField(max_length=200)
    school_code = models.CharField(max_length=20, unique=True, blank=True, null=True)
    date_added_at = models.DateTimeField(default=timezone.now, verbose_name="Date Added")
    date_updated_at = models.DateTimeField(auto_now=True, verbose_name="Date Updated")

    def __str__(self):
        return self.name

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