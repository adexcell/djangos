# Generated by Django 2.2.2 on 2019-06-14 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_apple'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nfs', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Samsung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fastcharge', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Xiaomi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hyroscope', models.BooleanField()),
            ],
        ),
    ]
