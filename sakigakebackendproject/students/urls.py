from django.urls import path
from .views import StudentsListView, AddStudentView, StudentDetailView

urlpatterns =[
    path("students/", StudentsListView.as_view(), name="student_list_view"),
    path("add_student/",AddStudentView.as_view(), name="add_student" ),
    path("students/<int:id>/", StudentDetailView.as_view(), name="student_detail_view"),  
]