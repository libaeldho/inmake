# Generated by Django 4.1.4 on 2023-07-11 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mailing_address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=10)),
                ('course', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('reason_to_join', models.CharField(max_length=200)),
                ('checklist', models.CharField(max_length=200)),
                ('agree_terms', models.BooleanField(default=False)),
            ],
        ),
    ]
