from django.contrib import admin
from django.urls import path

from src.devices.api.views import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', api.urls),
]
