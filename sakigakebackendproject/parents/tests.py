from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Parent

class ParentTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.parent_data = {
            'first_name': 'Alice',
            'last_name': 'Kamau',
            'email_address': 'alice@gmail.com',
            'phone_number': '+9876543210'
        }
        self.parent = Parent.objects.create(**self.parent_data)

    def test_get_parents_list(self):
        url = reverse('parents_list_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_parent(self):
        updated_data = {
            'first_name': 'Alice',
            'last_name': 'Kamau',
            'email_address': 'alice@gmail.com',
            'phone_number': '+25476543210'
        }
        response = self.client.put(reverse('parents_detail_view', args=[self.parent.id]), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.parent.refresh_from_db()  
        self.assertEqual(self.parent.first_name, 'Alice')
        self.assertEqual(self.parent.last_name, 'Kamau')
        self.assertEqual(self.parent.email_address, 'alice@gmail.com')
        self.assertEqual(self.parent.phone_number, '+9876543210')

    def test_create_parent(self):
        parent_data = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email_address': 'jane@gmail.com',
            'phone_number': '+9876543210'
        }
        response = self.client.post(reverse('parents_list_view'), data=parent_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Parent.objects.count(), 1)  
        self.assertEqual(Parent.objects.last().first_name, 'Alice')

    def test_get_parent_detail(self):
        url = reverse('parents_detail_view', args=[self.parent.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.parent_data['first_name'])

    def test_retrieve_invalid_parent(self):
        non_existent_parents_id = 9999
        self.url = f'/parents/{non_existent_parents_id}/'
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_parent(self):
        url = reverse('parents_detail_view', args=[self.parent.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Parent.objects.count(), 0)    
    
    def test_delete_invalid_parent(self):
        non_existent_parent_id = 9999
        self.url = f'/students/{non_existent_parent_id}/'
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)