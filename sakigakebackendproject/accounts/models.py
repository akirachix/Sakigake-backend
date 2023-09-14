from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import serializers
from django.contrib.auth import authenticate

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True , default=1)
    school_name = models.CharField(max_length=100 , default=1)
    phone_number = models.CharField(max_length=20 , default=1)
    password = models.CharField(max_length=128 , default=1)
    confirm_password = models.CharField(max_length=128 , default=1)
    
    groups = models.ManyToManyField (
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'school_name', 'phone_number', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")
        
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)

            if not user:
                raise serializers.ValidationError("Invalid username or password.")
        else:
            raise serializers.ValidationError("Must include 'username' and 'password'.")

        attrs['user'] = user
        return attrs


# from django.contrib.auth.models import AbstractUser, Group, Permission
# from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     groups = models.ManyToManyField(Group, related_name='custom_users')
#     user_permissions = models.ManyToManyField(Permission, related_name='custom_users')

# class Teachers(AbstractUser):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     phone_number = PhoneNumberField(unique=True, region='IR')
#     location = models.CharField(max_length=100)
#     created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
#     groups = models.ManyToManyField(Group, related_name='healthworkers')
#     user_permissions = models.ManyToManyField(Permission, related_name='healthworkers')