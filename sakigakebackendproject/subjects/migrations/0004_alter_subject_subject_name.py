# Generated by Django 4.2.5 on 2023-09-12 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0003_subject_subject_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject_name',
            field=models.CharField(choices=[('1', 'English'), ('2', 'Kiswahili'), ('3', 'Mathematics'), ('4', 'Integrated Science'), ('5', 'Social Studies'), ('6', 'Business Studies'), ('7', 'Agriculture'), ('8', 'Pre-technical and Pre-Career Studies'), ('9', 'Religious Studies Education')], max_length=100),
        ),
    ]
