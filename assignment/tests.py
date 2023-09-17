from django.test import TestCase
from django.contrib.auth.models import User  
from shop.models import Shop  
from .models import Assignment

class AssignmentModelTestCase(TestCase):
    def setUp(self):
        
        self.shop = Shop.objects.create(name="Test Shop")

        self.assignment = Assignment.objects.create(
            topic="Test Assignment",
            competency="Test Competency",
            task="Test Task",
            materials=["Material 1", "Material 2"],
            category=self.shop,
            due_date=None,  
            date_added_at=None,  
            date_updated_at=None,  
        )

    def test_assignment_str(self):
        self.assertEqual(str(self.assignment), "Test Assignment")

    def test_assignment_attributes(self):
        
        self.assertEqual(self.assignment.topic, "Test Assignment")
        self.assertEqual(self.assignment.competency, "Test Competency")
        self.assertEqual(self.assignment.task, "Test Task")
        self.assertListEqual(self.assignment.materials, ["Material 1", "Material 2"])
        self.assertEqual(self.assignment.category, self.shop)

  

    def tearDown(self):
        self.shop.delete()
        self.assignment.delete()
