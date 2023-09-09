from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  
from school.models import School
from .serializers import SchoolSerializer


class SchoolListView(APIView):

    def get(self, request):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
       serializer = SchoolSerializer(data=request.data)
       if serializer.is_valid():
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailView(APIView):
    def get(self, request , id , format=None):
        school = School.objects.get(id=id)
        serializer = SchoolSerializer(school)
        return Response(serializer.data)
   
    def get(self, request, id, format=None):
        school = School.objects.get(id=id)
        
        serializer = SchoolSerializer(school)
        
        return Response(serializer.data)


    def put(self, request, id, format=None):
           school = School.objects.get(id=id)
           serializer = SchoolSerializer(school, data=request.data) 
           if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_200_OK) 
           return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    
    
    def delete(self , request , id, format=None):
        school = School.objects.get(id=id)
        school.delete()
        return Response("School deleted" , status=status.HTTP_204_NO_CONTENT)
    