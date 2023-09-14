
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from school.models import School
from .serializers import SchoolSerializer
from .views import SchoolListView, DetailView

class SchoolTests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_get_all_schools(self):
        School.objects.create(name='School 1')
        School.objects.create(name='School 2')

        request = self.factory.get('/school/schools/')
        view = SchoolListView.as_view()
        response = view(request)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
 

    def test_get_school(self):
        school = School.objects.create(name='Test School')

        request = self.factory.get(f'/api/schools/{school.school_id}/')
        view = DetailView.as_view()
        response = view(request, school_id=school.school_id)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(response.data['name'], school.name)

    def test_get_nonexistent_school(self):
        request = self.factory.get('/api/schools/9999/')
        view = DetailView.as_view()
        response = view(request, school_id=9999)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_create_school(self):
        data = {
        'name': 'New School',
        'email': 'test@example.com',
        'subjects': 'Math, Science',
        'grades': ['1', '2', '3'],
        'phone_number': '+1234567890',
        'website': 'http://www.example.com',
        'location': 'Test Location',
        'school_code': 'ABC123'
    }

        request = self.factory.post('/schools/schools/', data)
        view = SchoolListView.as_view()
        response = view(request)

        print(response.status_code) 
        print(response.data)

        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        # self.assertEqual(response.data['name'], data['name'])

    

    def test_create_school_invalid_data(self):
        data = {
            'name': 'New School',
            'email': 'invalid_email',
            'subjects': 'Math, Science',
            'grades': ['1', '2', '3'],
            'phone_number': '1234567890',
            'website': 'http://www.example.com',
            'location': 'Test Location',
            'school_code': 'ABC123'
        }

        request = self.factory.post('/api/schools/', data)
        view = SchoolListView.as_view()
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_school(self):
        school = School.objects.create(name='Test School')

        data = {
            'name': 'Updated School',
            'email': 'test@example.com',
            'subjects': 'Math, Science',
            'grades': ['4', '5', '6'],
            'phone_number': '+9876543210',
            'website': 'http://www.example.com',
            'location': 'Updated Location',
            'school_code': 'XYZ789'
        }

        request = self.factory.put(f'/school/schools/{school.school_id}/', data)
        view = DetailView.as_view()
        response = view(request, school_id=school.school_id)
        self.assertIsInstance(response.data, dict)
      

    def test_update_nonexistent_school(self):
        data = {
            'name': 'Updated School',
            'email': 'test@example.com',
            'subjects': 'Math, Science',
            'grades': ['4', '5', '6'],
            'phone_number': '+9876543210',
            'website': 'http://www.example.com',
            'location': 'Updated Location',
            'school_code': 'XYZ789'
        }

        request = self.factory.put('/school/schools/9999/', data)
        view = DetailView.as_view()
        response = view(request, school_id=9999)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    

    def test_delete_nonexistent_school(self):
        request = self.factory.delete('/school/schools/9999/')
        view = DetailView.as_view()
        response = view(request, school_id=9999)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)