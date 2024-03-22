from rest_framework.serializers import ModelSerializer, SerializerMethodField, ReadOnlyField
from ..models import Subjectss, StaffUser
from django.contrib.auth.models import User

class StaffSerializer(ModelSerializer):
    class Meta:
        model = StaffUser
        fields = ['staff']


class UserSerializer(ModelSerializer):
    staff = StaffSerializer()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'staff']

class SubjectSerializer(ModelSerializer):
    teachers = UserSerializer(many=True)
    student = UserSerializer(many=True)
    class Meta:
        model = Subjectss
        fields = ['name','full_name','teachers','student']