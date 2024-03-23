from django.contrib import admin
from .models import (
    StaffUser,Topic,Teachers,Marks
)

admin.site.register([
    StaffUser,Teachers,Topic,Marks   
])
