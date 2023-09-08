from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from assignment.models import Assignment
from notification.models import Notification

class AssignmentViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.assignment_data = {'title': 'Test Assignment', 'description': 'Test Description'}

    def test_create_assignment(self):
        response = self.client.post('/assignments/', self.assignment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_assignments(self):
        Assignment.objects.create(title='Assignment 1', description='Description 1')
        Assignment.objects.create(title='Assignment 2', description='Description 2')

        response = self.client.get('/assignments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_delete_assignment(self):
        assignment = Assignment.objects.create(title='Assignment to delete', description='Description to delete')
        response = self.client.delete(f'/assignments/{assignment.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class NotificationViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.notification_data = {'message': 'Test Notification'}

    def test_get_notification(self):
        notification = Notification.objects.create(message='Test Notification Message')
        response = self.client.get(f'/notifications/{notification.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Test Notification Message')

    def test_update_notification(self):
        notification = Notification.objects.create(message='Initial Message')
        updated_data = {'message': 'Updated Message'}
        response = self.client.put(f'/notifications/{notification.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Updated Message')
