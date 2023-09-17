from django.urls import path
from .views import ParentsListView, ParentDetailView
# ParentLoginView

urlpatterns =[
    path("parents/", ParentsListView.as_view(), name="parents_list_view"),
    path("parents/<int:id>/", ParentDetailView.as_view(), name="parents_detail_view"),
    path("add_parent/", ParentsListView.as_view(), name="add_parent"),
    # path("parent_login/", ParentLoginView.as_view(), name="parent_login"),
]