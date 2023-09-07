from django import forms
from  .models import Parents

class ParentsUploadForm(forms.ModelForm):
    class Meta:
        model = Parents
        fields = "__all__"