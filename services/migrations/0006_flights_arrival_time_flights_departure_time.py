# Generated by Django 5.0.7 on 2024-09-26 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_remove_flights_desc_remove_flights_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='flights',
            name='arrival_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flights',
            name='departure_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
