from django.urls import path

from.views import TeacherListView,TeacherDetailView
urlpatterns=[
    path("teachersList/", TeacherListView.as_view(),name="teachers_list_view"),
    path("teachersDetail/<int:id>/", TeacherDetailView.as_view(),name="teachers_detail_view"),
]