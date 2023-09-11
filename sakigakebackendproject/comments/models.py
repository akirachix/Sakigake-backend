from django.db import models

class Comment(models.Model):
    # assignment = models.ForeignKey('Assignment', on_delete=models.CASCADE)
    commentor = models.CharField(max_length=255)
    # user = models.ForeignKey(Parent, on_delete=models.CASCADE)
    content = models.TextField()   
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.commentor} - {self.created_at}"
