# Generated by Django 5.0.7 on 2024-10-04 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_alter_list_check_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='img',
            field=models.CharField(max_length=9999),
        ),
    ]
