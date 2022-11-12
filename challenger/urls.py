"""challenger URL Configuration"""
from django.contrib import admin
from django.urls import path, include

from challenger.api_docs import api_v1


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_v1)),
]
