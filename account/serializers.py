# from rest_framework import serializers
import re
from .models import School
# from rest_framework import serializers
# from .models import School
# from django.contrib.auth import authenticate

# class SchoolSerializer(serializers.ModelSerializer):
#     confirm_password = serializers.CharField(max_length=200, write_only=True)

#     class Meta:
#         model = School
#         fields = ('school_name', 'email_address', 'phonenumber', 'create_password', 'confirm_password')

#     def validate_email_address(self, value):
      
#         if School.objects.filter(email_address=value).exists():
#             raise serializers.ValidationError("Email address already exists.")
#         return value

#     def validate_confirm_password(self, value):
      
#         create_password = self.initial_data.get('create_password')
#         if value != create_password:
#             raise serializers.ValidationError("Passwords do not match.")
#         return value

#     def validate_create_password(self, value):
#         if not re.search(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$', value):
#             raise serializers.ValidationError("Password must contain at least 1 uppercase letter, 1 lowercase letter, 1 digit, and 1 special character (@#$%^&+=), and be at least 8 characters long.")
#         return value

#     def validate_phonenumber(self, value):
     
#         if len(value) < 10:
#             raise serializers.ValidationError("Phone number must be at least 10 digits long.")
#         return value
    


# class LoginSerializer(serializers.Serializer):
#     password = serializers.CharField(max_length=200)
#     phonenumber = serializers.CharField(max_length=20)

#     def validate(self, attrs):
#         password = attrs.get('password')
#         phonenumber = attrs.get('phonenumber')

#         # Validate password and phone number against the user's credentials
#         # Assuming you have a User model with password and phonenumber fields
#         user = User.objects.filter(phonenumber=phonenumber).first()
#         if user:
#             if not user.check_password(password):
#                 raise serializers.ValidationError("Invalid password.")
#         else:
#             raise serializers.ValidationError("User not found.")
        
#         attrs['user'] = user
#         return attrs
from rest_framework import serializers

class SchoolSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=200, write_only=True)

    class Meta:
        model = School
        fields = ('id', 'school_name', 'email_address', 'phonenumber', 'create_password', 'confirm_password')

    def validate_email_address(self, value):
        if School.objects.filter(email_address=value).exists():
            raise serializers.ValidationError("Email address already exists.")
        return value

    def validate_confirm_password(self, value):
        create_password = self.initial_data.get('create_password')
        if value != create_password:
            raise serializers.ValidationError("Passwords do not match.")
        return value

    def validate_create_password(self, value):
        if not re.search(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$', value):
            raise serializers.ValidationError("Password must contain at least 1 uppercase letter, 1 lowercase letter, 1 digit, and 1 special character (@#$%^&+=), and be at least 8 characters long.")
        return value

    def validate_phonenumber(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Phone number must be at least 10 digits long.")
        return value

# serializers.py

from rest_framework import serializers
from .models import Parent, Teacher

# class TeacherSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=100)
#     last_name = serializers.CharField(max_length=100)
#     phone_number = serializers.CharField(max_length=20)
#     password = serializers.CharField(max_length=100)
#     school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())

#     def create(self, validated_data):
#         return Teacher.objects.create(**validated_data)

from rest_framework import serializers

# class ParentRegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Parent
#         fields = ['first_name', 'last_name', 'email_address', 'phone_number', 'create_password', 'confirm_password']

# class TeacherRegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Teacher
#         fields = ['first_name', 'last_name', 'email_address', 'phone_number', 'create_password', 'confirm_password']




from rest_framework import serializers
from .models import School, Parent, Teacher

class ParentRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = Parent
        fields = ['first_name', 'last_name', 'email_address', 'phone_number', 'create_password', 'confirm_password']

    def create(self, validated_data):
        validated_data.pop('confirm_password')  # Remove confirm_password from validated_data
        parent = Parent.objects.create(**validated_data)
        return parent

class TeacherRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email_address', 'phone_number', 'create_password', 'confirm_password']

    def create(self, validated_data):
        validated_data.pop('confirm_password')  # Remove confirm_password from validated_data
        teacher = Teacher.objects.create(**validated_data)
        return teacher

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



