# Generated by Django 4.1.4 on 2023-01-06 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0003_rename_descri_travel_des'),
    ]

    operations = [
        migrations.RenameField(
            model_name='travel',
            old_name='des',
            new_name='des1',
        ),
    ]
