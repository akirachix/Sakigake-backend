# Generated by Django 3.2.7 on 2023-10-06 06:45

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subject', '__first__'),
        ('shop', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('competency', models.CharField(max_length=100)),
                ('task', models.TextField()),
                ('resources', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), size=None)),
                ('due_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_added_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.subject')),
            ],
        ),
    ]
