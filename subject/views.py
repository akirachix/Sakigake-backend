from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Subject
from .serializers import SubjectSerializer

class SubjectListView(APIView):
    def get(self, request):
        try:
            subjects = Subject.objects.all()
            serializer = SubjectSerializer(subjects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            serializer = SubjectSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SubjectDetailView(APIView):
    def get(self, request, subject_id, format=None):
        try:
            subject = Subject.objects.get(id=subject_id)
            serializer = SubjectSerializer(subject)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Subject.DoesNotExist:
            return Response("Subject not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, subject_id, format=None):
        try:
            subject = Subject.objects.get(id=subject_id)
            serializer = SubjectSerializer(subject, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Subject.DoesNotExist:
            return Response("Subject not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, subject_id, format=None):
        try:
            subject = Subject.objects.get(id=subject_id)
            subject.delete()
            return Response("Subject deleted", status=status.HTTP_204_NO_CONTENT)
        except Subject.DoesNotExist:
            return Response("Subject not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)