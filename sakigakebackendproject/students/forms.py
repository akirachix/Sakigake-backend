from django import forms
from  .models import Students

class StudentUploadForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"
