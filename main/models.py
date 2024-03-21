from django.db import models
from django.contrib.auth.models import User


class StaffUser(models.Model):
    staff_choice = [
        ('TEACHER','teacher'),
        ('STUDENT','student'),
        ('ADMIN','admin')
    ]
    staff = models.CharField(max_length=8,choices=staff_choice, default='TEACHER')
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='staff')


class Subject(models.Model):
    name = models.CharField(max_length=30)
    full_name = models.CharField(max_length=90)
    student = models.ManyToManyField(User, related_name='subject')

class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher')
    subjects = models.ManyToManyField(Subject,related_name='teacher')

