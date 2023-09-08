from django.urls import path

from api.views import AssignmentViewTests, NotificationViewTests


urlpatterns = [
    path('assignments/', AssignmentViewTests.as_view(), name='assignment-list'),
    path('assignments/<int:id>/', AssignmentViewTests.as_view(), name='assignment-detail'),
    path('notifications/<int:id>/', NotificationViewTests.as_view(), name='notification-detail'),
]
