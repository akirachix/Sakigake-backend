from django.urls import path
from .views import CommentListAPIView, EditCommentAPIView

urlpatterns = [
    path('list/', CommentListAPIView.as_view()),
    path('edit/<int:id>/', EditCommentAPIView.as_view()),
]