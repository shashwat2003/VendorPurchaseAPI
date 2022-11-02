from rest_framework import status

responses = {"UNAUTHENTICATED": {"error": "You are not Autheticated!"}}

statusCodes = {"UNAUTHENTICATED": status.HTTP_401_UNAUTHORIZED}
