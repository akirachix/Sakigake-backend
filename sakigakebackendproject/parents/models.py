from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# from school.models import School

class Parent(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email_address = models.EmailField(null=True)
    # school = models.ManyToManyField(School)
    phone_number = PhoneNumberField(unique=True, region='KE')
    date_added_at = models.DateTimeField(auto_now_add=True)
    date_updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    




    #  objects = ParentManager()

# class ParentManager(models.Manager):
#     def validate(self, data):
#         if "email_address" in data and "first_name" in data:
#             return True
#         return False

#     def validate_update(self, parent_id, updated_data):
#         try:
#             parent = self.get(id=parent_id)
#             if "first_name" in updated_data:
#                 parent.first_name = updated_data["first_name"]
#                 parent.save()
#                 return True
#             return False
#         except Parent.DoesNotExist:
#             return False   