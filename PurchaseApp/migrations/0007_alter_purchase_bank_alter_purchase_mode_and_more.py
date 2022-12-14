# Generated by Django 4.1.2 on 2023-01-08 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VendorApp', '0011_alter_bankdetail_ifsc'),
        ('UserApp', '0007_delete_bankdetail'),
        ('PurchaseApp', '0006_alter_purchase_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='bank',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='VendorApp.bankdetail'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='mode',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='UserApp.info'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='payment_amount',
            field=models.CharField(default=None, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='payment_remarks',
            field=models.TextField(default=None, null=True),
        ),
    ]
