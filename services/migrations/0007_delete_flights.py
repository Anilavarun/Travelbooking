# Generated by Django 5.0.7 on 2024-09-27 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_flights_arrival_time_flights_departure_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='flights',
        ),
    ]