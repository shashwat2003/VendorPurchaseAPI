from django.db import models


def upload_msme_certificate(instance, filename):
    print("Heeell")
    print(instance)
    print(filename)
    return "msme_certificates/{0}/{1}".format(instance.name, filename)


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
    pan_number = models.CharField(max_length=10, blank=True, default="")
    gst_number = models.CharField(max_length=20, blank=True, default="")
    msme_certified = models.BooleanField(default=False)
    msme_certificate = models.FileField(blank=True,
                                        default="",
                                        upload_to=upload_msme_certificate)
    payment_cycle = models.ForeignKey("UserApp.Info",
                                      on_delete=models.SET_NULL,
                                      null=True,
                                      related_name="cyclic_vendors")


class BankDetail(models.Model):
    acc_name = models.CharField(max_length=40)
    acc_number = models.CharField(max_length=30, primary_key=True, unique=True)
    ifsc = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=40)
    bank_address = models.CharField(max_length=100)
    vendor = models.ForeignKey("VendorApp.Vendor",
                               null=True,
                               on_delete=models.SET_NULL)
    added_by = models.ForeignKey("UserApp.User", on_delete=models.PROTECT)
