from django.urls import path
from .views import GradeDetailView, GradesListView


urlpatterns =[
    path("grades/", GradesListView.as_view(), name="grades_list_view"),
    path("class/<int:id>/", GradeDetailView.as_view(), name="grades_detail_view"),
    path("add_class/", GradesListView.as_view(), name="add_grades"),
]