# Generated by Django 4.1.7 on 2023-03-28 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_userprofile_address_line_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='longitude',
        ),
    ]
