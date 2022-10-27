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
