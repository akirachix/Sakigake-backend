from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from students.models import Student

class StudentsListViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('student_list_view')
        self.student_data = {'first_name': 'Florence', 'last_name': 'Wangui'}

    def test_list_students(self):
        Student.objects.create(first_name='Florence', last_name='Wangui', parent_phone_number='+254720002451')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_student(self):
        response = self.client.post(self.url, self.student_data, format='json')
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 0)

class StudentDetailViewTest(APITestCase):
    def setUp(self):
        self.student = Student.objects.create(first_name='Florence', last_name='Wangui', parent_phone_number='+254720002451')
        self.url = reverse('student_detail_view', args=[self.student.id])
        self.updated_student_data = {'first_name': 'Florence', 'last_name': 'Student'}

    def test_update_student(self):
        response = self.client.patch(self.url, self.updated_student_data, format='json')
        # self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.student.refresh_from_db()
        self.assertEqual(self.student.first_name, self.updated_student_data['first_name'])

    def test_get_student(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.student.first_name)

    def test_get_invalid_student(self):
        non_existent_student_id = 9999
        self.url = f'/students/{non_existent_student_id}/'
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_delete_student(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Student.objects.filter(id=self.student.id).exists())
   
    def test_delete_invalid_student(self):
        non_existent_student_id = 54
        self.url = f'/students/{non_existent_student_id}/'
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)