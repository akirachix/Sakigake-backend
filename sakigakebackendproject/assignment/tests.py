from django.test import TestCase
from django.utils import timezone
from .models import Assignment

class AssignmentModelTestCase(TestCase):

    def setUp(self):
        # Create a sample Assignment instance for testing
        self.assignment = Assignment(
            topic="Test Assignment",
            competency="Test Competency",
            task="Test Task",
            materials="Test Materials",
            category="Test Category",
            due_date=timezone.now(),
            date_added_at=timezone.now(),
            date_updated_at=timezone.now()
        )

    def test_assignment_creation(self):
        # Test if the Assignment instance was created successfully
        self.assertIsInstance(self.assignment, Assignment)

    def test_assignment_fields(self):
        # Test individual fields of the Assignment instance
        self.assertEqual(self.assignment.topic, "Test Assignment")
        self.assertEqual(self.assignment.competency, "Test Competency")
        self.assertEqual(self.assignment.task, "Test Task")
        self.assertEqual(self.assignment.materials, "Test Materials")
        self.assertEqual(self.assignment.category, "Test Category")

    def test_assignment_due_date(self):
        # Test if the due_date is a valid DateTime object
        self.assertTrue(timezone.is_aware(self.assignment.due_date))

    def test_assignment_date_added_updated(self):
        # Test if date_added_at and date_updated_at are valid DateTime objects
        self.assertTrue(timezone.is_aware(self.assignment.date_added_at))
        self.assertTrue(timezone.is_aware(self.assignment.date_updated_at))
