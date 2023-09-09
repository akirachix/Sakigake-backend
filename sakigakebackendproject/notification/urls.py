from django.urls import path
from api.views import NotificationView


urlpatterns = [
    
    path('notifications/<int:id>/', NotificationView.as_view()),
]
