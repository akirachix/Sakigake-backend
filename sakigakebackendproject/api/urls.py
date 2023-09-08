from django.urls import path
from .views import AssignmentView, NotificationView

urlpatterns = [
    path('assignments/', AssignmentView.as_view(), name='assignment-list'),
    path('assignments/<int:id>/', AssignmentView.as_view(), name='assignment-detail'),
    path('notifications/<int:id>/', NotificationView.as_view(), name='notification-detail'),
]
