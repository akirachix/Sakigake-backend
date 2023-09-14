# from django.urls import path
# from .views import SignupView, LoginView, LogoutView, UserListAPIView,UserDetailAPIView

# urlpatterns = [
#     path('signup/', SignupView.as_view(), name='signup'),
#     path('login/', LoginView.as_view(), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('users/', UserListAPIView.as_view(), name='user-list'),
#     path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
# ]

from django.urls import path
from . import views
​
urlpatterns = [
    path('ngo/signup/', views.ngo_signup, name='ngo-signup'),
    path('ngo/logout/', views.ngo_logout, name='ngo-logout'),
    path('customusers/', views.CustomUserList.as_view(), name='customuser-list'),
    path('customusers/<int:pk>/', views.CustomUserDetail.as_view(), name='customuser-detail'),
    path('healthworkers/', views.HealthworkerList.as_view(), name='healthworker-list'),
    path('healthworkers/<int:pk>/', views.healthworker_detail, name='healthworker-detail'),
    path('healthworker/signup/', views.healthworker_signup, name='healthworker-signup'),
    path('healthworker/logout/', views.healthworker_logout, name='healthworker-logout'),
    path('healthworker/login/', views.healthworker_login, name='healthworker-login'),
    path('ngo/login/', views.ngo_login, name='ngo-login'),
]