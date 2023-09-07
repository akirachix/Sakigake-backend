from django import forms
from .models import Comment

class CommentUploadForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["user", "content","parent_comment"]