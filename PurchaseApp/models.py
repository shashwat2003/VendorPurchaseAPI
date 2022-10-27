from django.db import models


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
    invoice = models.FileField()
    gst_perc = models.FloatField(default=0.0)
    remarks = models.TextField()
    payment_status = models.BooleanField(default=False)
    payment_date = models.DateField()
    payment_amount = models.CharField(max_length=9)
    payment_remarks = models.TextField()
    added_by = models.ForeignKey("UserApp.User",
                                 on_delete=models.SET_NULL,
                                 null=True)
    timestamp = models.DateTimeField(auto_add=True)


class Contract(models.Model):
    vendor = models.ForeignKey("VendorApp.Vendor",
                               on_delete=models.SET_NULL,
                               null=True)
    from_date = models.DateField()
    to_date = models.DateField()
    remarks = models.TextField()
    added_by = models.ForeignKey("UserApp.User",
                                 on_delete=models.SET_NULL,
                                 null=True)
    contract = models.FileField()
    timestamp = models.DateTimeField(auto_add=True)