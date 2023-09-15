from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from .models import Shop
from .serializers import ShopSerializer

class ShopAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.shop_data = {
            'name': 'Test Shop',
            'location': 'Test Location',
            'phone_number': '+1234567890',
            'category': 'Test Category',
        }
        self.shop = Shop.objects.create(**self.shop_data)

    def test_create_shop(self):
        url = reverse('shop')
        response = self.client.post(url, self.shop_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_shops(self):
        url = reverse('shop')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_shop(self):
        url = reverse('shop_detail', kwargs={'id': self.shop.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_shop(self):
        updated_data = {
            'name': 'Updated Shop Name',
            'location': 'Updated Shop Location',
            'phone_number': '+2546543210',
            'category': 'Updated Category',
        }
        url = reverse('shop_detail', kwargs={'id': self.shop.id})
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_shop(self):
        url = reverse('shop_detail', kwargs={'id': self.shop.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_410_GONE)
