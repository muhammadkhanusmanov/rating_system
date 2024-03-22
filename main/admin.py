from django.contrib import admin
from .models import (
    StaffUser,Topic,Teachers
)

admin.site.register([
    StaffUser,Teachers,Topic       
])
