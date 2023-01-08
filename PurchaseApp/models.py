from django.db import models


def upload_contract(instance, filename):
    return "contracts/{0}/{1}".format(instance.vendor.name, filename)


def upload_invoice(instance, filename):
    return "contracts/{0}/{1}".format(instance.vendor.name, filename)


# Create your models here.
class Purchase(models.Model):
    vendor = models.ForeignKey("VendorApp.Vendor",
                               on_delete=models.SET_NULL,
                               null=True)
    category = models.ForeignKey("VendorApp.Category",
                                 on_delete=models.SET_NULL,
                                 null=True)
    po = models.CharField(max_length=20)
    inv_date = models.DateField()
    inv_number = models.CharField(max_length=20)
    inv_amount = models.CharField(max_length=9)
    invoice = models.FileField(blank=True,
                               default="",
                               upload_to=upload_invoice)
    gst_perc = models.FloatField(default=0.0)
    mode = models.ForeignKey("UserApp.Info",
                             null=True,
                             on_delete=models.SET_NULL,
                             default=None)
    bank = models.ForeignKey("VendorApp.BankDetail",
                             null=True,
                             on_delete=models.SET_NULL,
                             default=None)
    remarks = models.TextField()
    payment_status = models.BooleanField(default=False)
    payment_date = models.DateField(default=None, null=True)
    payment_amount = models.CharField(max_length=9, default=None, null=True)
    payment_remarks = models.TextField(default=None, null=True)
    added_by = models.ForeignKey("UserApp.User",
                                 on_delete=models.SET_NULL,
                                 null=True)
    timestamp = models.DateTimeField(auto_now=True)


class Contract(models.Model):
    vendor = models.ForeignKey("VendorApp.Vendor",
                               on_delete=models.SET_NULL,
                               null=True)
    from_date = models.DateField()
    to_date = models.DateField()
    remarks = models.TextField(blank=True, default="")
    added_by = models.ForeignKey("UserApp.User",
                                 on_delete=models.SET_NULL,
                                 null=True)
    contract = models.FileField(blank=True,
                                default="",
                                upload_to=upload_contract)
    timestamp = models.DateTimeField(auto_now=True)