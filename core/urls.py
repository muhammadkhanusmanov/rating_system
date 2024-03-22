from django.contrib import admin
from django.urls import path
from main.views import Signin,GetUser
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/login/', Signin.as_view()),
    path('student/subjects/',GetUser.as_view())
] + static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
