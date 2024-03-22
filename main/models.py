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

class Teachers(models.Model):
    image = models.ImageField(upload_to='teacher_image/')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Topic(models.Model):
    name = models.CharField(max_length=30)
    full_name = models.CharField(max_length=90)
    img = models.ImageField(upload_to='subject_images/')
    teachers = models.ManyToManyField(Teachers)
    student = models.ManyToManyField(User, related_name='subject')


