from django.shortcuts import render
from students.models import Student
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentsSerializer
from rest_framework.views import APIView

# Create your views here.

class StudentsListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentsSerializer(students, many=True)
        return Response(serializer.data)

class AddStudentView(APIView):
    http_method_names = ['post'] 

    def post(self, request, format=None):
        student_data = request.data
        serializer = StudentsSerializer(data=student_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class StudentDetailView(APIView):
    http_method_names = ['get', 'put', 'delete'] 

    def get(self, request, id, format=None):
        student = Student.objects.get(id=id)
        serializer = StudentsSerializer(student)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        student = Student.objects.get(id=id)
        serializer = StudentsSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        student = Student.objects.get(id=id)
        student.delete()
        return Response("Student Removed", status=status.HTTP_204_NO_CONTENT)