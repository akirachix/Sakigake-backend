from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20 ,default=1)
   
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

class School(models.Model):
    school_name = models.CharField(max_length=200)
    email_address = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=200)
    create_password = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200)


    def __str__(self):
        return self.school_name

    def add_teacher(self, first_name, last_name, email_address, phone_number, create_password ):
        teacher = Teacher.objects.create(
            first_name=first_name,
            last_name=last_name,
            email_address=email_address,
            phone_number=phone_number,
            create_password=create_password,
            school=self
        )
        return teacher

    def add_parent(self, first_name, last_name, email_address, phone_number , create_password):
        parent = Parent.objects.create(
            first_name=first_name,
            last_name=last_name,
            email_address=email_address,
            phone_number=phone_number,
            create_password= create_password ,
            school=self
        )
        return parent
    

class Teacher(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email_address = models.EmailField(null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE , default=1)
    is_class_teacher = models.BooleanField(default=False)
    phone_number = models.CharField(unique=True, max_length=200)
    create_password = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200)

    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Parent(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email_address = models.EmailField(null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE , default=1)
    phone_number = models.CharField(unique=True, max_length=200)
    create_password = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
    
    
