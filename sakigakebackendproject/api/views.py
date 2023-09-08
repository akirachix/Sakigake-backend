from django.shortcuts import render
from api.serializers import AssignmentSerializer, NotificationSerializer
from assignment.models import Assignment
from notification.models import Notification
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView

class AssignmentView(APIView):
    def get(self, request):
        assignment = Assignment.objects.all()
        serializer = AssignmentSerializer(assignment, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = AssignmentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400)
    
    def delete(self, request, id, format=None):
        assignment = Assignment.objects.get(id=id)
        assignment.delete()
        return Response("Assignment Removed from the database", status= status.HTTP_204_NO_CONTENT)
    
class NotificationView(APIView):

    def get(self, request, id, format=None):
        notification = Notification.objects.get(id=id)
        serializer = NotificationSerializer(notification)
        return Response(serializer.data)
    def put(self, request, id, format=None):
        notification = Notification.objects.get(id=id)
        serializer = Notification(notification, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400)
    
    