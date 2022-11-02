from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from VendorPurchaseAPI.constant_functions import responses, statusCodes
from .models import Vendor
from .serializers import *
# Create your views here.


class VendorView(APIView):

    def get(self, request: Request):
        if request.user.is_authenticated and request.user.role.name == "admin":
            vendors = Vendor.objects.all()
            serializer = VendorSerializer(vendors, many=True)
            return Response(serializer.data)
        else:
            return Response(responses.UNAUTHENTICATED,
                            statusCodes.UNAUTHENTICATED)

    def post(self, request: Request):
        if request.user.is_authenticated and request.user.role.name == "admin":
            serializer = VendorSerializer(data=request.data)
            if serializer.is_valid():
                print(serializer.data)
            else:
                print(serializer.errors)
        else:
            return Response(responses.UNAUTHENTICATED,
                            statusCodes.UNAUTHENTICATED)
