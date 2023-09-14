from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from parents.models import Parent
from .serializers import ParentsSerializer

class ParentListViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("parents-list")
        self.parent_details = {'firstname': 'Beth', 'lastname': 'Wangui', 'phone_number': '0792797189'}

    def test_get_parents_list(self):
        response  =self.client.get(self.url)
        parents = Parent.objects.all()
        serializer = ParentsSerializer(parents, many =True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_add_parent(self):
        response = self.client.post(self.url, self.parent_details)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Parent.objects.count(), 1)
        self.assertEqual(Parent.objects.get().first_name, self.parent_details['firstname'])
        self.assertEqual(Parent.objects.get().last_name, self.parent_details['lastname'])

class ParentDetailViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.parent = Parent.objects.create(first_name='Joan', last_name = 'Njiru')  
        self.url = reverse('parent-detail', args=[self.parent.id])
        self.updated_parent_data = {'first_name': 'Joan', 'last_name': 'Njiru'}  

    def test_get_parent_detail(self):
        response = self.client.get(self.url)
        serializer = ParentsSerializer(self.parent)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_parent(self):
        response = self.client.put(self.url, self.updated_parent_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.parent.refresh_from_db()
        self.assertEqual(self.parent.name, self.updated_parent_data['first_name'])
        self.assertEqual(self.parent.age, self.updated_parent_data['last_name'])

    def test_delete_parent(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Parent.objects.filter(id=self.parent.id).exists())