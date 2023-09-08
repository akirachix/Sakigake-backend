from rest_framework.serializers import ModelSerializer
from teachers import Teacher


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'




