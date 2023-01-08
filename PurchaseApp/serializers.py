from rest_framework import serializers
from .models import *


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Contract


class ContractViewSerliazer(serializers.ModelSerializer):
    contract_url = serializers.SerializerMethodField()

    class Meta:
        fields = "__all__"
        model = Contract
        depth = 1

    def get_contract_url(self, instance):
        return instance.contract.url if bool(instance.contract) else None


class PurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Purchase


class PurchaseViewSerliazer(serializers.ModelSerializer):
    invoice_url = serializers.SerializerMethodField()

    class Meta:
        fields = "__all__"
        model = Purchase
        depth = 1

    def get_invoice_url(self, instance):
        print(instance.invoice)
        return instance.invoice.url if bool(instance.invoice) else None
