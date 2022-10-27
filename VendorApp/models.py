from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, unique=True, primary_key=True)


class Vendor(models.Model):
    name = models.CharField(max_length=50)
    location = models.ForeignKey("UserApp.Info",
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 related_name="loc_vendors")
    category = models.ManyToManyField(Category, related_name="vendors")
    bank_details = models.ManyToManyField("UserApp.BankDetail",
                                          related_name="vendors")
    pan_number = models.CharField(max_length=10)
    gst_number = models.CharField(max_length=20, unique=True, primary_key=True)
    msme_certified = models.BooleanField(default=False)
    msme_certificate = models.FileField()
    payment_cycle = models.ForeignKey("UserApp.Info",
                                      on_delete=models.SET_NULL,
                                      null=True,
                                      related_name="cyclic_vendors")