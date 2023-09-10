from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Parent  
from .serializers import ParentsSerializer 


class ParentsAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.parent_data = {
            "first_name": "Beth",
            "last_name": "Wangui",
            "email_address": "wangui@gmail.com",
            "phone_number": "0720002451"
        }
        self.parent = Parent.objects.create(**self.parent_data)
        self.url_list = reverse('parents_list_view')  
        self.url_detail = reverse('parents_detail_view', args=[self.parent.id])  

    def test_list_parents(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_parent(self):
        response = self.client.post(self.url_list, self.parent_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_parent(self):
        invalid_data = {
           
            "first_name": "x",
            "last_name": "y",
            "email_address": "z",  
        }
        response = self.client.post(self.url_list, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_parent(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_parent(self):
        updated_data = {
            
            "first_name": "Jane",
            "last_name": "Wanjiku",
            "email_address": "jane@gmail.com",
            "phone_number": "+25470000000"
        }
        response = self.client.put(self.url_detail, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_parent(self):
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)