from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Assignment

class AssignmentTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.assignment_data = {"title": "", "description": ""}
        self.assignment = Assignment.objects.create(title="", description="")

    def test_create_assignment(self):
        response = self.client.post(reverse("assignment-list"), self.assignment_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_assignment_list(self):
        response = self.client.get(reverse("assignment-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_assignment_detail(self):
        response = self.client.get(reverse("assignment-detail", args=[self.assignment.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_assignment(self):
        updated_data = {"title": "Updated Assignment", "description": "Updated Description"}
        response = self.client.put(reverse("assignment-detail", args=[self.assignment.id]), updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_assignment(self):
        response = self.client.delete(reverse("assignment-detail", args=[self.assignment.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
