from django.urls import path
from . import views

from.views import TeacherListView,TeacherDetailView
urlpatterns=[
    path("teachersList/", TeacherListView.as_view(),name="teachers_list_view"),
    path("teachersDetail/<int:id>/", TeacherDetailView.as_view(),name="teachers_detail_view"),
    # path('login/', views.teacher_login, name='teacher_login'),
    # path('logout/', views.teacher_logout, name='teacher_logout'),
    # path('teachers/<int:id>/change-password/', views.TeacherDetailView.as_view(), name='teacher_change_password'),
]