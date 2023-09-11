from django.test import TestCase
from .models import School
class SchoolModelTest(TestCase):

    def test_generate_school_code(self):
        # Create a School instance
        school = School.objects.create(
            name="Example School",
            email="example@example.com",
            website="http://www.example.com",
            location="Example Location"
        )

        # Call the generate_school_code method
        school.generate_school_code()

        # Check if the school_code field is not empty
        self.assertIsNotNone(school.school_code)

    def test_phone_number_validation(self):
        # Create a School instance with an invalid phone number
        school = School.objects.create(
            name="Invalid School",
            email="invalid@example.com",
            website="http://www.invalid.com",
            location="Invalid Location",
            phone_number="invalid"
        )

        # Try to save the instance and expect a ValidationError
        with self.assertRaises(ValidationError):
            school.save()

    # Add more test methods for other model functionality as needed
