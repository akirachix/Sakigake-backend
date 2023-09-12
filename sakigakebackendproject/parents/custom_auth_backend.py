# from django.contrib.auth.backends import BaseBackend
# from parents.models import Parent  

# class PhonePasswordAuthBackend(BaseBackend):
#     def authenticate(self, request, phone_number=None, password=None):
#         try:
#             parent = Parent.objects.get(phone_number=phone_number)
#             if parent.user.check_password(password):
#                 return parent.user
#         except Parent.DoesNotExist:
#             pass
#         return None

#     def get_user(self, user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None