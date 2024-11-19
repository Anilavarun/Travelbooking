# Generated by Django 5.0.7 on 2024-10-14 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_rooms_roomlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomlist',
            name='category',
        ),
        migrations.DeleteModel(
            name='rooms',
        ),
        migrations.AddField(
            model_name='list',
            name='first',
            field=models.CharField(max_length=9999, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='second',
            field=models.CharField(max_length=9999, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='third',
            field=models.CharField(max_length=9999, null=True),
        ),
        migrations.DeleteModel(
            name='roomlist',
        ),
    ]