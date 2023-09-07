from django.db import models
from students.models import Students

# Create your models here.
class Parents(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=10)
    student_name = models.CharField(max_length=32)
    password = models.CharField(max_length=16)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='parents')

    def __str__(self):
        return self.first_name.last_name