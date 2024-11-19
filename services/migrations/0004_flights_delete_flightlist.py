# Generated by Django 5.0.7 on 2024-09-24 14:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_flightlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='flights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=9999, unique=True)),
                ('slug', models.SlugField(max_length=9999, unique=True)),
                ('img', models.CharField(max_length=9999)),
                ('price', models.IntegerField()),
                ('desc', models.TextField()),
                ('available', models.BooleanField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.categ')),
            ],
        ),
        migrations.DeleteModel(
            name='flightlist',
        ),
    ]
