from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Student  
from .serializers import StudentsSerializer

class StudentsAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.student_data = {
            "first_name": "Flo",
            "last_name": "Wangui",
            "parent_phone_number": "+254720002451"
        }
        self.student = Student.objects.create(**self.student_data)
        self.url_list = reverse('student_list_view') 
        self.url_detail = reverse('student_detail_view', args=[self.student.id])

    def test_list_students(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_student(self):
        response = self.client.post(self.url_list, self.student_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_student(self):
        invalid_data = {
            "first_name": "Anna",
            "last_name": "Lisa",
            "parent_phone_number": "+254722222",  
        }
        response = self.client.post(self.url_list, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_student(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_student(self):
        updated_data = {
            "first_name": "Ian",
            "last_name": "Wangui",
            "parent_phone_number": "+2547111111",
        }
        response = self.client.put(self.url_detail, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_student(self):
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)