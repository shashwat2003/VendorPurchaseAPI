from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    profile_photo = models.FileField(default=None, null=True)
    role = models.ForeignKey("Role",
                             default="user",
                             on_delete=models.SET_NULL,
                             null=True)


class Role(models.Model):
    name = models.CharField(max_length=10, unique=True, primary_key=True)


class Info(models.Model):
    type = models.CharField(max_length=20)
    value = models.CharField(max_length=20)


class BankDetail(models.Model):
    acc_name = models.CharField(max_length=40)
    acc_number = models.CharField(max_length=30, primary_key=True, unique=True)
    ifsc = models.CharField(max_length=10)
    bank_name = models.CharField(max_length=40)
    bank_address = models.CharField(max_length=100)
    vendor = models.ForeignKey("VendorApp.Vendor",
                               null=True,
                               on_delete=models.SET_NULL)
