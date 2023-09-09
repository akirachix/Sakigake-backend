from django.db import models

class Notification(models.Model):
    # sender = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    # recipient = models.ForeignKey('Parent', on_delete=models.CASCADE)
    preview = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.preview

