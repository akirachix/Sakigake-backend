from django.db import models

# Create your models here.
class Notification(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE, editable=True)
    parent = models.ForeignKey(Parent,on_delete=models.CASCADE, editable=True)
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE, editable=True)
    preview = models.CharField(max_length=255) 
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Notification from {self.teacher} to {self.parent}'
    
