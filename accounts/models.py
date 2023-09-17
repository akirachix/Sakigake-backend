from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    school_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30 , default=1)
    phone_number = PhoneNumberField()
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')

class Teacher(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number =PhoneNumberField(max_length=20, )
    location = models.CharField(max_length=100)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    groups = models.ManyToManyField(Group, related_name='teachers')
    user_permissions = models.ManyToManyField(Permission, related_name='teachers')

class Parent(AbstractUser):
    first_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    last_name = models.CharField(max_length=30)
    phone_number = PhoneNumberField(unique=True, region='KE')
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    groups = models.ManyToManyField(Group, related_name='parents')
    user_permissions = models.ManyToManyField(Permission, related_name='parents')