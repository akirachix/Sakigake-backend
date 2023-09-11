# Generated by Django 4.2.5 on 2023-09-11 06:31

from django.db import migrations, models
import django.utils.timezone
import phonenumber_field.modelfields
import school.models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20230909_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='school',
            name='date_updated',
        ),
        migrations.AddField(
            model_name='school',
            name='date_added_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Added'),
        ),
        migrations.AddField(
            model_name='school',
            name='date_updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Updated'),
        ),
        migrations.AlterField(
            model_name='school',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, validators=[school.models.validate_phone_number]),
        ),
        migrations.AlterField(
            model_name='school',
            name='school_code',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
