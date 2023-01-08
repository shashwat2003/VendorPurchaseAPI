from rest_framework import status

responses = {"UNAUTHENTICATED": {"error": "You are not Autheticated!"}}

statusCodes = {
    "UNAUTHENTICATED": status.HTTP_401_UNAUTHORIZED,
    "ERROR": status.HTTP_400_BAD_REQUEST,
    "SUCCESS": status.HTTP_200_OK,
    "CREATED": status.HTTP_201_CREATED,
    "ACCEPTED": status.HTTP_202_ACCEPTED
}
