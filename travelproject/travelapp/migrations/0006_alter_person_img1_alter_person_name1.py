# Generated by Django 4.1.4 on 2023-01-07 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0005_rename_travel_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='img1',
            field=models.ImageField(upload_to='PIC'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name1',
            field=models.CharField(max_length=200),
        ),
    ]
