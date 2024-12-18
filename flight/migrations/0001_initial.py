# Generated by Django 5.0.7 on 2024-09-27 07:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('airline', models.CharField(max_length=100)),
                ('plane', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_no', models.CharField(max_length=20, unique=True)),
                ('passengers', models.IntegerField()),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('CONFIRMED', 'Confirmed'), ('PENDING', 'Pending'), ('CANCELLED', 'Cancelled')], default='PENDING', max_length=10)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.flight')),
            ],
        ),
    ]
