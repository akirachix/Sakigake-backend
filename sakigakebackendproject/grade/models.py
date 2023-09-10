from django.db import models

class CompetencyBasedGrade(models.Model):
    GRADE_CHOICES = (
        (1, 'Grade 1'),
        (2, 'Grade 2'),
        (3, 'Grade 3'),
        (4, 'Grade 4'),
        (5, 'Grade 5'),
        (6, 'Grade 6'),
    )
    
    description = models.CharField(max_length=100)
    grade = models.PositiveIntegerField(choices=GRADE_CHOICES)
    # subjects = models.ManyToManyField(Subject, related_name='grades')
    # teachers = models.ManyToManyField(Teacher, related_name='grades')
    # assignments = models.ManyToManyField(Assignment, related_name='grades')

  
