from django.db import models


def upload_msme_certificate(instance, filename):
    return "msme_certificates/{0}/{1}".format(instance.id, filename)


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