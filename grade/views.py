from django.shortcuts import render
from account.models import Teacher
from rest_framework.response import Response
from rest_framework import status
from .serializers import GradeSerializer
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from .models import Grade


class GradesListView(APIView):
    def get(self, request):
        grades = Grade.objects.all()
        serializer = GradeSerializer(grades, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = GradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GradeDetailView(APIView):
    def get(self, request, grade_id):
        try:
            grade = Grade.objects.get(id=id)
        except ObjectDoesNotExist:
            return Response("Grade not found.", status=status.HTTP_404_NOT_FOUND)
        
        serializer = GradeSerializer(grade)
        return Response(serializer.data)
    
    def put(self, request, grade_id):
        try:
            grade = Grade.objects.get(id=id)
        except ObjectDoesNotExist:
            return Response("Grade not found.", status=status.HTTP_404_NOT_FOUND)
        
        serializer = GradeSerializer(grade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,id):
        try:
            grade = Grade.objects.get(id=id)
        except ObjectDoesNotExist:
            return Response("Grade not found.", status=status.HTTP_404_NOT_FOUND)
        
        grade.delete()
        return Response("Grade removed.", status=status.HTTP_204_NO_CONTENT)