# Generated by Django 2.2.2 on 2019-07-08 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0004_auto_20190708_1233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asus',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='samsung',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='xiaomi',
            name='phone',
        ),
    ]
