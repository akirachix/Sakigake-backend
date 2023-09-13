from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory
from .models import Teacher
from .serializers import TeacherSerializer
from .views import TeacherListView, TeacherDetailView


class TeacherListViewTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = TeacherListView.as_view()
        self.url = '/teachers/'

    def test_get_teachers(self):
        Teacher.objects.create(first_name='Alice', last_name='Warter', email='alicewarter@gmail.com')
        Teacher.objects.create(first_name='John', last_name='Kimani', email='johnkimani@gmail.com')

        request = self.factory.get(self.url)
        response = self.view(request)

        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_teacher(self):
        data = {
            'first_name': 'Dave',
            'last_name': 'Kipepeo',
            'email': 'kipepeodave@gmail.com',
            'phone_number': '+123456789',
            'password': '23',
            'is_class_teacher': False
        }

        request = self.factory.post(self.url, data)
        response = self.view(request)

       


class TeacherDetailViewTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = TeacherDetailView.as_view()
        self.url = '/teachers/{}/'

    def test_get_teacher(self):
        teacher = Teacher.objects.create(first_name='John', last_name='Doe', email='john@example.com')
        url = self.url.format(teacher.id)

        request = self.factory.get(url)
        response = self.view(request, id=teacher.id)

        serializer = TeacherSerializer(teacher)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
