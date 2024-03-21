from django.contrib import admin
from django.urls import path
from ..main.views import Signin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Signin.as_view())
]
