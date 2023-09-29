from django.db import models
from assignment.models import Assignment
from django.conf import settings
from account.models import Parent
from account.models import CustomUser




class Comment(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE,null=True)
    commentor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()   
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.commentor} - {self.created_at}"
