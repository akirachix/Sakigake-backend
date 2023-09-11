from django.urls import path
from .views import ParentsListView, ParentDetailView, AddParentView

urlpatterns =[
    path("parents/", ParentsListView.as_view(), name="parents_list_view"),
    path("parents/<int:id>/", ParentDetailView.as_view(), name="parents_detail_view"),
    path("add_parent/", AddParentView.as_view(), name="add_parent"),
]