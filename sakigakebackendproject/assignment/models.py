from django.db import models

# Create your models here.
class Assignment(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE, editable=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, editable=True)
    homework = models.TextField()
    resources = models.CharField(max_length=32)
    due_date = models.DateTimeField()
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()

    def __str__(self):
        return self.resources

