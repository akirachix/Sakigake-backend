from django.urls import path
from .views import delete_comment, comments_list,edit_comment,upload_comment

urlpatterns = [
    path('comments/',comments_list, name='comment_list_view'),
    path('comments/upload/', upload_comment, name="upload_commnets_view"),
    path('comments/edit/<int:id>', edit_comment, name="edit_comment_view"),
    path('comments/delete/<int:id>', delete_comment, name="delete_comment_view"),
    
]
