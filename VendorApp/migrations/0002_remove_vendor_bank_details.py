# Generated by Django 4.1.2 on 2022-11-01 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VendorApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='bank_details',
        ),
    ]