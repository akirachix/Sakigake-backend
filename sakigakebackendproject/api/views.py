from django.shortcuts import render
from students.models import Student
from parents.models import Parent
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentsSerializer, ParentsSerializer
from rest_framework.views import APIView


# Create your views here.

class StudentsListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentsSerializer(students, many = True)
        return Response(serializer.data)
    
class AddStudentView(APIView):
    def post(self, request, format=None):
        student_data = request.data
        serializer = StudentsSerializer(data=student_data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class StudentDetailView(APIView):
    def get(self, request, id, format=None):
        students = Student.objects.get(id=id)
        serializer = StudentsSerializer(students)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        students = Student.objects.get(id=id)
        serializer = StudentsSerializer(students, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status = status.HTTP_400)
    
    def delete(self, request, id, format=None):
        students = Student.objects.get(id=id)
        students.delete()
        return Response("Student Removed ", status= status.HTTP_204_NO_CONTENT)
    

class ParentsListView(APIView):
    def get(self, request):
        parents = Parent.objects.all()
        serializer = ParentsSerializer(parents, many = True)
        return Response(serializer.data)
    
   
class AddParentView(APIView):
    def post(self, request, format=None):
        parents_data = request.data
        serializer = ParentsSerializer(data=parents_data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class ParentDetailView(APIView):
    def get(self, request, id, format=None):
        parents = Parent.objects.get(id=id)
        serializer = ParentsSerializer(parents)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        parents = Parent.objects.get(id=id)
        serializer = ParentsSerializer(parents, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status = status.HTTP_400)
    
    def delete(self, request, id, format=None):
        parents = Parent.objects.get(id=id)
        parents.delete()
        return Response("Parent Removed ", status= status.HTTP_204_NO_CONTENT)