from django.urls import path
from .views import ParentsListView, ParentDetailView

urlpatterns =[
    path("parents/", ParentsListView.as_view(), name="parents_list_view"),
    path("parents/<int:id>/", ParentDetailView.as_view(), name="parents_detail_view"),
]