# Generated by Django 3.2.12 on 2023-09-11 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_auto_20230911_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='subjects',
            field=models.CharField(default='', max_length=50),
        ),
    ]
