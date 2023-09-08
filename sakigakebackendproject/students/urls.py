from django.urls import path
from .views import students_list_view, student_update_view, students_details_view

urlpatterns = [
    path("students/list/", students_list_view, name="students_list_view"),
    path("students/<int:id>/",students_details_view, name="students_detail_view"),
    path("students/edit/<int:id>/", student_update_view, name = "students_update"),
]