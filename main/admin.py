from django.contrib import admin
from .models import (
    StaffUser,Subjects
)

admin.site.register([
    StaffUser,Subjects          
])
