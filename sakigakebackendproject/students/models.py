from django.db import models
# from phonenumbers import PhoneNumberField


class Student(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    # parent_phone_number = models.PhoneNumberField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    class_grade = models.CharField(max_length=32)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"