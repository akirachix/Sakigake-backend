from django.db import models
from accounts.views import UserListAPIView
from assignment.models import Assignment
from django.conf import settings
from parents.models import Parent
# from django.contrib.auth.models import User



class Comment(models.Model):
    assignment = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    commentor = models.ForeignKey(Parent, on_delete=models.CASCADE)
    content = models.TextField()   
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.commentor} - {self.created_at}"
