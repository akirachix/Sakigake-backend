from django.urls import path
from .views import (
    # ParentLogoutView,
    ParentLogoutView,
    SignupView,
    LoginView,
    SignoutView,
    SchoolListView,
    SchoolDetailView,
    ParentRegistrationView,
    TeacherLogoutView,
    TeacherRegistrationView,
    ParentLoginView,
    TeacherLoginView,
   
)

urlpatterns = [
    path('schools/signup/registered', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('signout/', SignoutView.as_view(), name='signout'),
    path('schools/', SchoolListView.as_view(), name='school-list'),
    path('schools/<int:pk>/', SchoolDetailView.as_view(), name='school-detail'),
    path('schools/<int:school_id>/parents/register/', ParentRegistrationView.as_view(), name='parent-registration'),
    path('schools/<int:school_id>/teachers/signup/', TeacherRegistrationView.as_view(), name='teacher-registration'),
    path('schools/parents/login/', ParentLoginView.as_view(), name='parent-login'),
    path('schools/teachers/signin/', TeacherLoginView.as_view(), name='teacher-login'),
    path('schools/parent/logout/', ParentLogoutView.as_view(), name='parent-logout'),
    path('schools/teacher/logout/', TeacherLogoutView.as_view(), name='teacher-logout'),
 
]
