# Generated by Django 5.0.7 on 2024-10-04 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_remove_list_room_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='checkin_date',
            new_name='check_date',
        ),
        migrations.RenameField(
            model_name='list',
            old_name='checkin_time',
            new_name='check_time',
        ),
    ]
