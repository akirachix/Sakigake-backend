from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from school.models import School
from .serializers import SchoolSerializer

class SchoolListView(APIView):
    def get(self, request):
        try:
            schools = School.objects.all()
            serializer = SchoolSerializer(schools, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response("An error occurred while fetching schools", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = SchoolSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
           
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
           
            return Response("An error occurred while creating a new school", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DetailView(APIView):
    def get(self, request, id, format=None):
        try:
            school = School.objects.get(id=id)
            serializer = SchoolSerializer(school)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except School.DoesNotExist:
            return Response("School not found", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id, format=None):
        try:
            school = School.objects.get(id=id)
            serializer = SchoolSerializer(school, data=request.data) 
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except School.DoesNotExist:
            return Response("School not found", status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id, format=None):
        try:
            school = School.objects.get(id=id)
            school.delete()
            return Response("School deleted", status=status.HTTP_204_NO_CONTENT)
        except School.DoesNotExist:
            return Response("School not found", status=status.HTTP_404_NOT_FOUND)
