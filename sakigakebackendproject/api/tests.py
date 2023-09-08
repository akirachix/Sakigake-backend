
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Teacher

class TeacherAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.teacher_data = {
            'first_name': 'Mary',
            'last_name': 'Kimani',
            'email': 'marykimani@gmail.com',
            'phone_number': '476345763249',
            'password': '#mary123',
            'is_class_teacher': False
        }
        self.teacher = Teacher.objects.create(**self.teacher_data)

    def test_teacher_list_view(self):
        response = self.client.get('/teachers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_teacher_create_view(self):
        response = self.client.post('/teachers/', self.teacher_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Teacher.objects.count(), 2)  # Assuming you had one teacher in the database already

    def test_teacher_detail_view(self):
        response = self.client.get(f'/teachers/{self.teacher.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.teacher_data['first_name'])

    def test_teacher_update_view(self):
        updated_data = {
            'first_name': 'Beatrice',
            'last_name': 'Goko',
            'email': 'gokobeatrice@gmail.com',
            'phone_number': '8584576372',
            'password': 'bea#123',
            'is_class_teacher': True
        }
        response = self.client.put(f'/teachers/{self.teacher.id}/', updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.teacher.refresh_from_db()
        self.assertEqual(self.teacher.first_name, updated_data['first_name'])

    def test_teacher_delete_view(self):
        response = self.client.delete(f'/teachers/{self.teacher.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Teacher.objects.filter(id=self.teacher.id).exists())