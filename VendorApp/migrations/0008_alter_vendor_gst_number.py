# Generated by Django 4.1.2 on 2022-11-02 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VendorApp', '0007_alter_vendor_category_alter_vendor_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='gst_number',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
