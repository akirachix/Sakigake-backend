from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import School
from .serializers import SchoolSerializer

class SchoolAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.school_data = {'name': 'Test School'}
        self.school = School.objects.create(name='Existing School')

    def test_create_school(self):
        response = self.client.post('/api/schools/', self.school_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(School.objects.count(), 2) 

    def test_list_schools(self):
        response = self.client.get('/api/schools/')
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

    def test_retrieve_school(self):
        response = self.client.get(f'/api/schools/{self.school.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Existing School')  

    def test_update_school(self):
        updated_data = {'name': 'Updated School'}
        response = self.client.put(f'/api/schools/{self.school.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(School.objects.get(id=self.school.id).name, 'Updated School') 

    def test_delete_school(self):
        response = self.client.delete(f'/api/schools/{self.school.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(School.objects.count(), 0) 
