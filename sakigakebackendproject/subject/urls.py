from django.urls import path
from.views import SubjectListView, SubjectDetailView
urlpatterns=[
    path("subjectsList/", SubjectListView.as_view(),name="subjects_list_view"),
    path("subjectsDetail/<int:subject_id>/", SubjectDetailView.as_view(),name="subjects_detail_view"),
]