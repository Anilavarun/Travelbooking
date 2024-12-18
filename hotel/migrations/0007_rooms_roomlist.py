# Generated by Django 5.0.7 on 2024-10-14 06:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_alter_list_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=99, null=True)),
                ('slug', models.SlugField(max_length=99, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='roomlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=99, null=True)),
                ('slug', models.SlugField(max_length=99, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('img', models.CharField(max_length=9999)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.hotels')),
            ],
        ),
    ]
