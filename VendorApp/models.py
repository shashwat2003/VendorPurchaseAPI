from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, unique=True, primary_key=True)


# class Vendor(models.Model):
#     # id = models.BigAutoField(primary_key=False)
#     name = models.CharField(max_length=50)
#     location = models.ForeignKey("UserApp.Info",
#                                  on_delete=models.SET_NULL,
#                                  null=True,
#                                  related_name="loc_vendors")
#     category = models.ManyToManyField(Category, related_name="vendors")
#     pan_number = models.CharField(max_length=10, blank=True, default="")
#     gst_number = models.CharField(max_length=20,
#                                   unique=True,
#                                   blank=True,
#                                   primary_key=True,
#                                   default="")
#     msme_certified = models.BooleanField(default=False)
#     msme_certificate = models.FileField(blank=True, default="")
#     payment_cycle = models.ForeignKey("UserApp.Info",
#                                       on_delete=models.SET_NULL,
#                                       null=True,
#                                       related_name="cyclic_vendors")


class Vendor(models.Model):
    name = models.CharField(max_length=50)
    location = models.ForeignKey("UserApp.Info",
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 related_name="loc_vendors")
    category = models.ManyToManyField(Category, related_name="vendors")
    pan_number = models.CharField(max_length=10, blank=True, default="")
    gst_number = models.CharField(max_length=20,
                                  unique=True,
                                  blank=True,
                                  default="")
    msme_certified = models.BooleanField(default=False)
    msme_certificate = models.FileField(blank=True, default="")
    payment_cycle = models.ForeignKey("UserApp.Info",
                                      on_delete=models.SET_NULL,
                                      null=True,
                                      related_name="cyclic_vendors")