from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Assignment
from .serializers import AssignmentSerializer

class AssigmentListView(APIView):
    def get(self,request):
        assignment = Assignment.objects.all()
        serializer =AssignmentSerializer(assignment, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk,format=None):
        assignment = self.get(pk,id=id)
        serializer = AssignmentSerializer(assignment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format = None):
        assignment = self.get(pk,id)
        assignment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
        

    
        




