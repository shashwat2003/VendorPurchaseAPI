from django.db import models


def upload_file(instance, filename):
    return "uploaded/{0}/{1}".format(instance.id, filename)


# Create your models here.
class UploadFile(models.Model):
    uploaded_by = models.ForeignKey("UserApp.User", on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now=True)
    file = models.FileField()