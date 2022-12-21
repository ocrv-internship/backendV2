from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('authapi.urls')),
    path('api/v1/', include('api.urls')),
]
