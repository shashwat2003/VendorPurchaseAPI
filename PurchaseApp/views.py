from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ContractSerializer, ContractViewSerliazer, PurchaseViewSerliazer, PurchaseSerializer
from .models import Contract, Purchase
from VendorPurchaseAPI.constant_functions import statusCodes, responses
from VendorApp.models import Vendor
from Common.models import UploadFile
from django.core.files.base import ContentFile
# Create your views here.


class PurchaseView(APIView):

    def get(self, request):
        if request.user.is_authenticated and request.user.role.name == "admin":
            purchases = Purchase.objects.all()
            serializer = PurchaseViewSerliazer(purchases, many=True)
            return Response(serializer.data)

        else:
            return Response(responses.get("UNAUTHENTICATED"),
                            statusCodes.get("UNAUTHENTICATED"))

    def post(self, request):
        if request.user.is_authenticated and request.user.role.name == "admin":
            data = request.data.copy()
            data["added_by"] = request.user.id
            vendor = Vendor.objects.filter(id=data.get("vendor", 0)).first()
            if vendor is None:
                return Response({"error": "Vendor not found!"},
                                statusCodes.get("ERROR"))

            cached_file = UploadFile.objects.filter(
                id=data.get("invoice", 0)).first()
            if cached_file:
                file = ContentFile(cached_file.file.read())
                file.name = cached_file.file.name
                data["invoice"] = file
            else:
                data.pop("invoice")
            data["inv_date"] = data.get("inv_date").split("T")[0]
            data["payment_date"] = data.get(
                "payment_date", None).split("T")[0] if data.get(
                    "payment_date", None) is not None else None
            serializer = PurchaseSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"success": "Purchase Added Successfully!"})
            else:
                print(serializer.errors)
                return Response(
                    {"error": "Please re-check the input provided!"},
                    statusCodes.get("ERROR"))
        else:
            return Response(responses.get("UNAUTHENTICATED"),
                            statusCodes.get("UNAUTHENTICATED"))


class ContractView(APIView):

    def get(self, request: Request):
        if request.user.is_authenticated and request.user.role.name == "admin":
            vendor = request.query_params.get("vendor", 0)
            if vendor == 0:
                contracts = Contract.objects.all()
                serializer = ContractViewSerliazer(contracts, many=True)
                return Response(serializer.data)
            else:
                vendor = Vendor.objects.filter(id=vendor).first()
                if vendor is None:
                    return Response({"error": "Vendor not found!"},
                                    statusCodes.get("ERROR"))
                contracts = Contract.objects.filter(vendor=vendor)
                return Response({"success": contracts.count()})
        else:
            return Response(responses.get("UNAUTHENTICATED"),
                            statusCodes.get("UNAUTHENTICATED"))

    def post(self, request: Request):
        if request.user.is_authenticated and request.user.role.name == "admin":
            data = request.data.copy()
            data["added_by"] = request.user.id
            vendor = Vendor.objects.filter(id=data.get("vendor", 0)).first()
            if vendor is None:
                return Response({"error": "Vendor not found!"},
                                statusCodes.get("ERROR"))

            cached_file = UploadFile.objects.filter(
                id=data.get("contract", 0)).first()
            if cached_file:
                file = ContentFile(cached_file.file.read())
                file.name = cached_file.file.name
                data["contract"] = file
            else:
                data.pop("contract")
            data["from_date"] = data.get("from_date").split("T")[0]
            data["to_date"] = data.get("to_date").split("T")[0]
            serializer = ContractSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"success": "Contract Added Successfully!"})
            else:
                print(serializer.errors)
                return Response(
                    {"error": "Please re-check the input provided!"},
                    statusCodes.get("ERROR"))
        else:
            return Response(responses.get("UNAUTHENTICATED"),
                            statusCodes.get("UNAUTHENTICATED"))
