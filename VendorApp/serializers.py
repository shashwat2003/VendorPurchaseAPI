from rest_framework.serializers import ModelSerializer, CharField
from .models import *


class VendorSerializer(ModelSerializer):

    class Meta:
        model = Vendor
        fields = "__all__"


class VendorViewSerializer(ModelSerializer):

    class Meta:
        model = Vendor
        fields = "__all__"
        depth = 1


class BankDetailSerializer(ModelSerializer):

    class Meta:
        model = BankDetail
        fields = "__all__"


class BankDetailViewSerializer(ModelSerializer):

    class Meta:
        model = BankDetail
        fields = "__all__"
        depth = 1