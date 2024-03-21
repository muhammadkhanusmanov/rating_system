from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.http import HttpRequest,JsonResponse,FileResponse
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication, BasicAuthentication


class Signin(APIView):
    authentication_classes = [BasicAuthentication]
    def post(self,request):
        user = request.user
        try:
            token,created = Token.objects.get_or_create(user = user)
            return Response({'Status': 'OK','Token': token.key},status=status.HTTP_200_OK)
        except:
            return Response({'Status': 'User not found', 'Token':None},status=status.HTTP_404_NOT_FOUND)