# Generated by Django 4.2.3 on 2023-07-14 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='graduation',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AddField(
            model_name='student',
            name='studying_year',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
