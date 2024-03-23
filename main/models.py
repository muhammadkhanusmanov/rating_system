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

    def __str__(self):
        return self.user.username

class Teachers(models.Model):
    image = models.ImageField(upload_to='teacher_image/')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Topic(models.Model):
    name = models.CharField(max_length=30)
    full_name = models.CharField(max_length=90)
    img = models.ImageField(upload_to='subject_images/')
    teachers = models.ManyToManyField(Teachers)
    student = models.ManyToManyField(User, related_name='subject')

    def __str__(self):
        return self.full_name

class Marks(models.Model):
    marks = models.CharField(max_length=255)
    comment = models.CharField(max_length=255,blank=True)
    semester = models.CharField(max_length=30)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, related_name='marks')
    student = models.ForeignKey(User, on_delete=models.CASCADE,related_name='marks')
    subject = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='marks')

    def __str__(self) -> str:
        return f'{self.teacher.user.username} - {self.subject.full_name}'


