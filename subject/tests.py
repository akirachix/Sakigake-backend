from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from .views import SubjectListView, SubjectDetailView
from .models import Subject


class SubjectListViewTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = SubjectListView.as_view()
        self.url = '/subjects/'

    def test_get_subjects(self):
        Subject.objects.create(subject_name='Math')
        Subject.objects.create(subject_name='Science')

        request = self.factory.get(self.url)
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['subject_name'], 'Math')
        self.assertEqual(response.data[1]['subject_name'], 'Science')

        data = {'subject_name': ''}

        request = self.factory.post(self.url, data)
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class SubjectDetailViewTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = SubjectDetailView.as_view()
        self.url = '/subjects/'

    def test_get_subject(self):
        subject = Subject.objects.create(subject_name='Math')

        request = self.factory.get(f'{self.url}{subject.id}/')
        response = self.view(request, subject_id=subject.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['subject_name'], 'Math')

    def test_get_nonexistent_subject(self):
        request = self.factory.get(f'{self.url}999/')
        response = self.view(request, subject_id=999)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, 'Subject not found')

  
    def test_update_nonexistent_subject(self):
        data = {'subject_name': 'Algebra'}

        request = self.factory.put(f'{self.url}999/', data)
        response = self.view(request, subject_id=999)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, 'Subject not found')