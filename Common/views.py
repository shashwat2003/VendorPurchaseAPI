from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .serializers import UploadFileSerializer
from VendorPurchaseAPI.constant_functions import statusCodes
# Create your views here.


class UploadFileView(APIView):

    def post(self, request: Request):
        serializer = UploadFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, statusCodes.get("SUCCESS"))
        else:
            return Response(serializer.errors, statusCodes.get("ERROR"))
