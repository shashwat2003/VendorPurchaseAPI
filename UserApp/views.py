from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import *
from django.contrib.auth import authenticate, login
from .models import *
# Create your views here.


class UserLoginView(APIView):

    def get(self, request: Request):
        if request.user.is_authenticated and request.user.is_active:
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
