# Generated by Django 3.2.7 on 2023-09-30 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='confirm_password',
            field=models.CharField(default='kite', max_length=200),
            preserve_default=False,
        ),
    ]
