# Generated by Django 4.1.2 on 2022-12-29 21:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('VendorApp', '0009_alter_vendor_msme_certificate'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankDetail',
            fields=[
                ('acc_name', models.CharField(max_length=40)),
                ('acc_number', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('ifsc', models.CharField(max_length=10)),
                ('bank_name', models.CharField(max_length=40)),
                ('bank_address', models.CharField(max_length=100)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='VendorApp.vendor')),
            ],
        ),
    ]
