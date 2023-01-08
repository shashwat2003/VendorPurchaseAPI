from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import *
from django.contrib.auth import authenticate, login, logout
from VendorPurchaseAPI.constant_functions import responses, statusCodes
from .models import *
from VendorApp.models import Category, Vendor
# Create your views here.


class UserLoginView(APIView):

    def get(self, request: Request):
        if request.user.is_authenticated and request.user.is_active:
            if request.query_params.get("action", "") == "logout":
                logout(request)
                return Response({"success": "Done!"})
            return Response({"verified": True})
        else:
            return Response({"verified": False})

    def post(self, request: Request):
        print(request.data.keys())
        if "email" in request.data.keys():
            user = User.objects.filter(
                email=request.data.get("email").strip()).first()
            if user is None:
                return Response({"error": "Invalid Username or Password..."},
                                status=HTTP_400_BAD_REQUEST)
            username = user.username
        else:
            username = request.data.get("username")
        print(username)
        user = authenticate(username=username,
                            password=request.data.get("password"))
        if user is not None:
            login(request, user)
            return Response({"success": "Login Success!"})
        else:
            return Response({"error": "Invalid Username or Password..."},
                            status=HTTP_400_BAD_REQUEST)


class InfoView(APIView):

    def get(self, request: Request):
        if request.user.is_authenticated and request.user.role.name == "admin":
            query_type = request.query_params.get("query", "").upper()
            data = []
            if query_type == "CATEGORY":
                vendor = Vendor.objects.filter(
                    id=request.query_params.get("vendor", 0)).first()
                if vendor is None:
                    for item in Category.objects.all():
                        data.append({
                            "value": item.name,
                            "label": item.name.upper()
                        })
                else:
                    for item in vendor.category.all():
                        data.append({
                            "value": item.name,
                            "label": item.name.upper()
                        })
            else:
                for item in Info.objects.filter(type=query_type):
                    data.append({"value": item.id, "label": item.value})
            return Response(data)
        else:
            return Response(responses.get("UNAUTHENTICATED"),
                            statusCodes.get("UNAUTHENTICATED"))