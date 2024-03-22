from rest_framework.serializers import ModelSerializer, SerializerMethodField, ReadOnlyField
from ..models import Topic, StaffUser,Teachers
from django.contrib.auth.models import User

class StaffSerializer(ModelSerializer):
    class Meta:
        model = StaffUser
        fields = ['staff']


class UserSerializer(ModelSerializer):
    staff = StaffSerializer()
    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'staff']

class TeacherSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Teachers
        fields = ['id','image','user']

class SubjectSerializer(ModelSerializer):
    teachers = TeacherSerializer(many=True)
    class Meta:
        model = Topic
        fields = ['id','name','full_name','img','teachers']