import re
from .models import School

from rest_framework import serializers

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'school_name', 'email_address', 'phonenumber', 'create_password')
        extra_kwargs = {'create_password': {'write_only': True}}



    def validate_email_address(self, value):
        if School.objects.filter(email_address=value).exists():
            raise serializers.ValidationError("Email address already exists.")
        return value



    def validate_create_password(self, value):
        if not re.search(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$', value):
            raise serializers.ValidationError("Password must contain at least 1 uppercase letter, 1 lowercase letter, 1 digit, and 1 special character (@#$%^&+=), and be at least 8 characters long.")
        return value

    def validate_phonenumber(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Phone number must be at least 10 digits long.")
        return value


from .models import School, Parent, Teacher

class ParentRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parent
        fields = ['id','first_name', 'last_name', 'email_address', 'phone_number', 'create_password']
        extra_kwargs = {'create_password': {'write_only': True}}




class TeacherRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ['id','first_name', 'last_name', 'email_address', 'phone_number', 'create_password']
        extra_kwargs = {'create_password': {'write_only': True}}


        

class ParentLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')

        if phone_number and password:
            parent = Parent.objects.filter(phone_number=phone_number).first()

            if not parent:
                raise serializers.ValidationError("Invalid phone number or password.")

            if not parent.create_password == password:
                raise serializers.ValidationError("Invalid phone number or password.")
        else:
            raise serializers.ValidationError("Phone number and password are required.")

        return attrs

class TeacherLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')

        if phone_number and password:
            teacher = Teacher.objects.filter(phone_number=phone_number).first()

            if not teacher:
                raise serializers.ValidationError("Invalid phone number or password.")

            if not teacher.create_password == password:
                raise serializers.ValidationError("Invalid phone number or password.")
        else:
            raise serializers.ValidationError("Phone number and password are required.")

        return attrs



