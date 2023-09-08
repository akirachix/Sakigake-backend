from django.urls import path
from .views import CommentUploadAPIView, CommentListAPIView, EditCommentAPIView

urlpatterns = [
    path('upload/', CommentUploadAPIView.as_view()),
    path('list/', CommentListAPIView.as_view()),
    path('edit/<int:id>/', EditCommentAPIView.as_view()),
]