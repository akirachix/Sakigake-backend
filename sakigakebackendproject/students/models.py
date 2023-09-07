from django.db import models

# Create your models here.
class  Students(models.Model):
    first_name = models.Model.CharField(max_length=32)
    last_name = models.Model.CharField(max_length=32)
    admission_id = models.CharField(max_length=32)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name.last_name