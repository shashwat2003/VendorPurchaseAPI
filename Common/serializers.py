from rest_framework.serializers import ModelSerializer
from .models import UploadFile


class UploadFileSerializer(ModelSerializer):

    class Meta:
        model = UploadFile
        fields = "__all__"