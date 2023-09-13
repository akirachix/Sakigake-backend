from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Shop
from .serializers import ShopSerializer

class ShopTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.shop_data = {"name": "Test Shop", "location": "Test Location"}
        self.shop = Shop.objects.create(name="Existing Shop", location="Existing Location")

    def test_create_shop(self):
        response = self.client.post(reverse("shop-list"), self.shop_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_shop_list(self):
        response = self.client.get(reverse("shop-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_shop_detail(self):
        response = self.client.get(reverse("shop-detail", args=[self.shop.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_shop(self):
        updated_data = {"name": "Updated Shop", "location": "Updated Location"}
        response = self.client.put(reverse("shop-detail", args=[self.shop.id]), updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_shop(self):
        response = self.client.delete(reverse("shop-detail", args=[self.shop.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
