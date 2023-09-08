from django.db import models
# from .models import Subject
# from .models import Grade
# from .models import School



class Teacher(models.Model):
    # school = models.ForeignKey('School', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    # subjects = models.ManyToManyField('Subject')
    # grades = models.ManyToManyField('Grade')
    password = models.CharField(max_length=255)
    is_class_teacher = models.BooleanField(default=False) 
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.first_name