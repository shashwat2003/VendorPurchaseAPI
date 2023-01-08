from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .serializers import UploadFileSerializer
from .models import UploadFile
from VendorPurchaseAPI.constant_functions import statusCodes
from django.core.files.storage import default_storage
# Create your views here.


class UploadFileView(APIView):

    def post(self, request: Request):
        data = request.data.copy()
        data["uploaded_by"] = request.user.id
        serializer = UploadFileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.instance)
            return Response(
                {
                    "file": serializer.instance.file.url,
                    "id": serializer.instance.id
                }, statusCodes.get("SUCCESS"))
        else:
            return Response(serializer.errors, statusCodes.get("ERROR"))

    def delete(self, request: Request):
        print(request.data)
        instance = UploadFile.objects.filter(
            id=request.data.get("id", 0)).first()
        if instance is None:
            return Response({"success": "File does not exists!"},
                            statusCodes.get("SUCCESS"))
        try:
            default_storage.delete(instance.file.path)
        except:
            pass
        instance.delete()
        return Response({"success": "Deleted!"}, statusCodes.get("ACCEPTED"))
