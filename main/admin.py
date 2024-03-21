from django.contrib import admin
from .models import (
    StaffUser,Subject,Teacher
)

admin.site.register([
    StaffUser,Subject,
    Teacher              
])
