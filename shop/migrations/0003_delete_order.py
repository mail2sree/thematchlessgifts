# Generated by Django 3.2.6 on 2021-08-11 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]