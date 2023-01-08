from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from VendorPurchaseAPI.constant_functions import responses, statusCodes
from Common.models import UploadFile
from .models import Vendor
from .serializers import *
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
# Create your views here.


class VendorView(APIView):

    def get(self, request: Request):
        if request.user.is_authenticated and request.user.role.name == "admin":
            vendors = Vendor.objects.all()
            serializer = VendorViewSerializer(vendors, many=True)
            return Response(serializer.data)
        else:
            return Response(responses["UNAUTHENTICATED"],
                            statusCodes["UNAUTHENTICATED"])

    def post(self, request: Request):
        if request.user.is_authenticated and request.user.role.name == "admin":
            data = request.data.copy()
            cached_file = UploadFile.objects.filter(
                id=data.get("msme_certificate", 0)).first()
            if cached_file:
                # with open(cached_file.file.path, "rb") as f:
                #     data["msme_certificate"] = File(f)
                file = ContentFile(cached_file.file.read())
                file.name = cached_file.file.name
                data["msme_certificate"] = file
            else:
                data.pop("msme_certificate")
            print(data)
            serializer = VendorSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                if cached_file:
                    try:
                        default_storage.delete(cached_file.file.path)
                    except:
                        pass
                    cached_file.delete()
                return Response({"success": "Vendor Added Successfully!"})
            else:
                return Response(
                    {"error": "Please re-check the input provided!"},
                    statusCodes["ERROR"])
        else:
            return Response(responses["UNAUTHENTICATED"],
                            statusCodes["UNAUTHENTICATED"])


class BankDetailsView(APIView):

    def get(self, request: Request):
        if request.user.is_authenticated and request.user.role.name == "admin":
            vendor = request.query_params.get("vendor", 0)
            if vendor == 0:
                details = BankDetail.objects.all()
                serializer = BankDetailViewSerializer(details, many=True)
            else:
                details = BankDetail.objects.filter(vendor=vendor)
                serializer = BankDetailSerializer(details, many=True)

            return Response(serializer.data, statusCodes.get("SUCCESS"))
        else:
            return Response(responses.get("UNAUTHENTICATED"),
                            statusCodes.get("UNAUTHENTICATED"))

    def post(self, request: Request):
        if request.user.is_authenticated and request.user.role.name == "admin":
            data = request.data.copy()
            if BankDetail.objects.filter(
                    acc_number=data.get("acc_number")).first() is not None:
                return Response(
                    {
                        "error":
                        "Bank Account with same account number already exists!"
                    }, statusCodes.get("ERROR"))
            data["added_by"] = request.user.id
            serializer = BankDetailSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"success": "Bank Details Added Successfully!"})
            else:
                print(serializer.errors)
                return Response(
                    {"error": "Please re-check the input provided!"},
                    statusCodes["ERROR"])
        else:
            return Response(responses["UNAUTHENTICATED"],
                            statusCodes["UNAUTHENTICATED"])