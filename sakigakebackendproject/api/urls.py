from django.urls import path
from api.views import AssignmentView,NotificationView


urlpatterns = [
    path('assignments/', AssignmentView.as_view()),
    path('assignments/<int:id>/', AssignmentView.as_view()),
    path('notifications/<int:id>/', NotificationView.as_view()),
]
