import json
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Assignment
from .serializers import AssignmentSerializer

class AssigmentView(APIView):
    
    def get (self,request):
        assignments= Assignment.objects.all()
        serializer = AssignmentSerializer(assignments, many=True)
        return Response(serializer.data)
        
    
    def post(self,request):
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class TestNotificationView(APIView):

    def post(self, request):
        try:
            assignment_data = json.loads(request.body)
            assignment = Assignment.objects.create(
                title=assignment_data.get('title', 'Sample Assignment'),
                due_date=assignment_data.get('due_date', '2023-09-30'),
            )
            self.send_assignment_notification(assignment)

            return Response({"message": "Test notification sent successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
         print("Error:", str(e))
         return Response({"error": "Test notification not sent"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

    def send_assignment_notification(self, assignment):

        parent_tokens = [parent.fcm_token for parent in assignment.parent.all()]
        notification_data = {
            "to": parent_tokens,
            "notification": {
                "title": "New Assignment",
                "body": f"Assignment: {assignment.title}\nDue Date: {assignment.due_date}",
            }
        }

        url = 'https://fcm.googleapis.com/fcm/send'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'key=BOXJHv96VE4rCIdGRz5yf-KvETMxMikPuplet1WB3a6Pra-RvpCJqniX5ZIKvAm4KyTfmXMyDfcVAcI769SpYGM', 
        }

        response = requests.post(url, headers=headers, data=json.dumps(notification_data))

        if response.status_code == 200:
            print("Notification sent successfully.")
        else:
            print("Failed to send notification. Status code:", response.status_code)
    
class AssignmentDetailView(APIView):
    def get(self,request,id,format=None):
        try:
            assignment = Assignment.objects.get(id=id)
            serializer = AssignmentSerializer(assignment)
            return Response(serializer.data)
        except Assignment.DoesNotExist:
            return Response({"error":"Assignment not found"},status=status.HTTP_404_NOT_FOUND)

    

    def put(self, request, id, format=None):
        try:
            assignment = Assignment.objects.get(id=id)
            serializer = AssignmentSerializer(assignment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Assignment.DoesNotExist:
            return Response({"error": "Assignment not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,id):
        try:
            assignment = Assignment.objects.get(id=id)
            assignment.delete()
            return Response ({"message":"Assignment deleted"}, status=status.HTTP_404_NOT_FOUND)
        except Assignment.DoesNotExist:
            return Response({"error":"Assignment not found"},status=status.HTTP_404_NOT_FOUND)
        

    
        

    
        




