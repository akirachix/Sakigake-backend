from django.urls import path

from assignment.views import AssigmentView, AssignmentDetailView



urlpatterns = [
    path('assignments/', AssigmentView.as_view() , name="assignment"),
    path('assignments/<int:id>/',AssignmentDetailView.as_view() , name="assignment_detail"), 
]
