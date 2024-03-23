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

from .models import Topic, Teachers, Marks
from .serialazers.serialazer import UserSerializer, SubjectSerializer,MarksSerializer


class Signin(APIView):
    authentication_classes = [BasicAuthentication]
    def post(self,request):
        user = request.user 
        try:
            token,created = Token.objects.get_or_create(user = user)
            return Response({'Status': user.staff.staff,'Token': token.key},status=status.HTTP_200_OK)
        except:
            return Response({'Status': 'User not found', 'Token':None},status=status.HTTP_404_NOT_FOUND)

class GetUser(APIView):
    authentication_classes = [TokenAuthentication]
    '''get subjects for a student'''
    def get(self, request):
        user = request.user
        subjects = Topic.objects.filter(student=user)
        subjects = SubjectSerializer(subjects,many=True)
        return Response(subjects.data)
    '''get teachers by subject id'''
    def post(self, request,id:str):
        lessons = Topic.objects.get(id=id)
        teachers = SubjectSerializer(lessons).data['teachers']
        return Response(teachers)


class MarksView(APIView):
    authentication_classes = [TokenAuthentication]
    '''put mark'''
    def put(self,request):
        user = request.user
        data = request.data
        teacher = Teachers.objects.get(user=data['teacher'])
        subject = Topic.objects.get(id=data['subject'])
        mark = Marks.objects.create(
                marks = data['marks'],
                comment = data.get('comment', None),
                semester = data['semester'],
                student = user,
                teacher = teacher,
                subject = subject,
            )
        mark.save()
        print(mark)
        return Response({'success': True})
        
        




