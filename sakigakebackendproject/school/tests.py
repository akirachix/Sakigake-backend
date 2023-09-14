from django.test import TestCase
from .models import School

class SchoolModelTestCase(TestCase):
    def test_generate_school_code(self):
   
        school = School(name='Utawala School')
        
        code = school.generate_school_code()
        
        self.assertEqual(len(code), 8)  
        self.assertTrue(code.isalnum())  
    def test_save_method(self):
        school = School(name='Utawala School')
        school.save()
        self.assertIsNotNone(school.school_code)

        
        saved_school = School.objects.get(pk=school.pk)
        self.assertEqual(school.school_code, saved_school.school_code)

        self.assertIsNotNone(saved_school.date_added_at)
        self.assertIsNotNone(saved_school.date_updated_at)

        school.name = 'Updated School'
        school.save()
        updated_school = School.objects.get(pk=school.pk)
        self.assertEqual(updated_school.name, 'Updated School')
        self.assertGreater(updated_school.date_updated_at, saved_school.date_updated_at)
