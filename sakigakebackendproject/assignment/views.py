from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Assignment
from .serializers import AssignmentSerializer

class AssigmentView(APIView):
    def get(self,request):
        try:
            assignment = Assignment.objects.all()
            serializer = AssignmentSerializer(assignment,many=True)
            return Response(serializer.data ,status=status.HTTP_200_OK)
        except Exception as e:
            return Response ({"error":"An error occurred while fetching assignments"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
    def post(self,request):
        try:
            serializer = AssignmentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":"An error occurred when creating a new assignment"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    
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
        

    
        

    
        




