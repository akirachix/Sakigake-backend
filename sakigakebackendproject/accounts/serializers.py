# from rest_framework import serializers
# from .models import CustomUser

# from rest_framework import serializers
# from django.contrib.auth import authenticate
# from .models import CustomUser


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = CustomUser(
#             username=validated_data['username'],
#             email=validated_data['email']
#         )
#         user.set_password(validated_data['password'])
#         user.save()

#         return user




# from rest_framework import serializers
# from django.contrib.auth import authenticate
# from .models import CustomUser

# class UserSerializer(serializers.ModelSerializer):
#     confirm_password = serializers.CharField(write_only=True)

#     class Meta:
#         model = CustomUser
#         fields = ['id', 'username', 'email', 'school_name', 'phone_number', 'password', 'confirm_password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         password = validated_data.pop('password')
#         confirm_password = validated_data.pop('confirm_password')
#         if password != confirm_password:
#             raise serializers.ValidationError("Passwords do not match.")
        
#         user = CustomUser(**validated_data)
#         user.set_password(password)
#         user.save()
#         return user

# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=150)
#     password = serializers.CharField(max_length=128, write_only=True)

#     def validate(self, attrs):
#         username = attrs.get('username')
#         password = attrs.get('password')

#         if username and password:
#             user = authenticate(request=self.context.get('request'), username=username, password=password)

#             if not user:
#                 raise serializers.ValidationError("Invalid username or password.")
#         else:
#             raise serializers.ValidationError("Must include 'username' and 'password'.")

#         attrs['user'] = user
#         return attrs
    
# class UserCreateSerializer(serializers.ModelSerializer):
#     confirm_password = serializers.CharField(write_only=True)

#     class Meta:
#         model = CustomUser
#         fields = ['id', 'username', 'email', 'school_name', 'phone_number', 'password', 'confirm_password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         password = validated_data.pop('password')
#         confirm_password = validated_data.pop('confirm_password')
#         if password != confirm_password:
#             raise serializers.ValidationError("Passwords do not match.")
        
#         user = CustomUser(**validated_data)
#         user.set_password(password)
#         user.save()
#         return user

# class UserUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'school_name', 'phone_number']

# #
from rest_framework import serializers
from .models import CustomUser, Teacher

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', )

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'username', 'email', 'first_name',  'phone_number', 'created_by')