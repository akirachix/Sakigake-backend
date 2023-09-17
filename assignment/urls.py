from django.urls import path

from assignment.views import AssigmentView, AssignmentDetailView, TestNotificationView



urlpatterns = [
    path('assignments/', AssigmentView.as_view() , name="assignment"),
    path('assignments/<int:id>/',AssignmentDetailView.as_view() , name="assignment_detail"), 
    path('test_notification/', TestNotificationView.as_view(), name='test-notification'),
]
