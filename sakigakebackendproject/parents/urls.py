from django.urls import path
from .views import parents_list_view, parents_details_view, parent_update_view

urlpatterns = [
    path("parents/list/", parents_list_view, name="parents_list_view"),
    path("parents/<int:id>/",parents_details_view, name="parents_detail_view"),
    path("parents/edit/<int:id>/", parent_update_view, name = "parents_update"),
]