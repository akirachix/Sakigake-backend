from django.db import models
from account.models import Parent

from assignment.models import Assignment

class AssignmentRecipient(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    notification_status = models.BooleanField(default=False)  

    class Meta:
        unique_together = ('assignment', 'parent')  
