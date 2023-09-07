from django.urls import path
from . import views

urlpatterns = [
    path('schools/', views.school_list, name='school_list'),
    path('schools/<int:school_id>/', views.school_details, name='school_details'),
    path('schools/<int:school_id>/delete/', views.delete_school, name='delete_school'),
]