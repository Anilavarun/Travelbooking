# Generated by Django 5.0.7 on 2024-10-15 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0009_remove_list_first_remove_list_second_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='deluxe',
            field=models.CharField(max_length=9999, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='executive',
            field=models.CharField(max_length=9999, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='fifth',
            field=models.CharField(max_length=999, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='first',
            field=models.CharField(max_length=999, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='four',
            field=models.TextField(max_length=99, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='fourth',
            field=models.CharField(max_length=999, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='honeymoon',
            field=models.CharField(max_length=9999, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='one',
            field=models.TextField(max_length=99, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='second',
            field=models.CharField(max_length=999, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='single',
            field=models.CharField(max_length=9999, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='sixth',
            field=models.CharField(max_length=999, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='third',
            field=models.CharField(max_length=999, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='three',
            field=models.TextField(max_length=99, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='two',
            field=models.TextField(max_length=99, null=True),
        ),
    ]
