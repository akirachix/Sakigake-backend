from rest_framework import serializers
from parents.models import Parent


class ParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = "__all__"
