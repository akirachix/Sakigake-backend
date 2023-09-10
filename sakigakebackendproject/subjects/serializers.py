from rest_framework import serializers
from .models import*
from  subjects.models  import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'




