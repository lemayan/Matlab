# Generated by Django 5.1.3 on 2024-11-19 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_appointment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='phonenumber',
            new_name='phone',
        ),
    ]