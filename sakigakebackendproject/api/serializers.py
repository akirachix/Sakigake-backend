from rest_framework import serializers

from students.models import Student
from parents.models import Parent


class ParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = "__all__"

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"