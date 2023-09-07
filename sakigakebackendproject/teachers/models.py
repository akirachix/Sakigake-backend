from django.db import models

class Teachers(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    subjects = models.ManyToManyField(Subjects) 
    grades = models.JSONField()
    password = models.CharField(max_length=128)
    is_class_teacher = models.BooleanField(default=False) # Indicates whether the teacher is a class teacher
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

def __str__(self):
      return f"{self.first_name} {self.last_name}"