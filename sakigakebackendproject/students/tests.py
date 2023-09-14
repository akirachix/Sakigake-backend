from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from students.models import Student
from .serializers import StudentsSerializer

class StudentsListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('students-list')

    def test_get_students(self):
        Student.objects.create(first_name = 'Flo', last_name = 'Wangui')
        Student.objects.create(first_name = 'Bridget', last_name = 'Nakakande')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        students = Student.objects.all()
        serializer = StudentsSerializer(students, many=True)
        self.assertEqual(response.data, serializer.data)

class AddStudentViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('add-student')

    def test_add_student(self):
        student_data = {'first_name': 'Kevine', 'last_name': 'Nzayanga'}
        response = self.client.post(self.url, student_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 1)

class StudentDetailViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.student = Student.objects.create(first_name='Kevine', last_name = 'Nzayanga')
        self.url = reverse('student-detail', args=[self.student.id])

    def test_get_student(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = StudentsSerializer(self.student)
        self.assertEqual(response.data, serializer.data)

    def test_update_student(self):
        updated_student_data = {'first_name': 'Kevine', 'last_name': 'Nzayanga'}
        response = self.client.put(self.url, updated_student_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.student.refresh_from_db()
        self.assertEqual(self.student.first_name, 'Kevine')
        self.assertEqual(self.student.last_name, 'Nzayanga')

    def test_delete_student(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Student.objects.filter(id=self.student.id).exists())