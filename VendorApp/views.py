from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from VendorPurchaseAPI.constant_functions import responses, statusCodes
from .models import Vendor
from .serializers import *
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
            serializer = VendorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"success": "Vendor Added Successfully!"})
            else:
                return Response({"error": serializer.errors},
                                statusCodes["ERROR"])
        else:
            return Response(responses["UNAUTHENTICATED"],
                            statusCodes["UNAUTHENTICATED"])
