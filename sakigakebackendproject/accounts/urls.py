# from django.urls import path
# from .views import register_user, user_login, user_logout

# # from .views import create_user, user_login, user_logout

# urlpatterns = [
#     path('register/', register_user, name='register'),
#     path('login/', user_login, name='login'),
#     path('logout/', user_logout, name='logout'),
# # ]
from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    # Add other URL patterns for your CRUD operations if needed.
]
