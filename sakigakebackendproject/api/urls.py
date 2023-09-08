from django.urls import path
from .views import StudentsListView, AddStudentView, StudentDetailView, ParentsListView, ParentDetailView

urls_patterns =[
    path("students/", StudentsListView.as_view(), name="student_list_view"),
    path("add_student/",AddStudentView.as_view(), name="add_student" ),
    path("students/<int:id>/", StudentDetailView.as_view(), name="student_detail_view"),
    path("parents/", ParentsListView.as_view(), name="parents_list_view"),
    path("parents/<int:id>/", ParentDetailView.as_view(), name="parents_detail_view"),
]
