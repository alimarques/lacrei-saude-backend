from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lacreisaude/v1/', include('lacreisaude.urls', namespace='lacreisaude')),
    path('lacreisaude-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
