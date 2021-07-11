from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static

from rest_framework.authtoken import views

from users.views import CustomObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('posts/', include('blogAPI.routers')),
    path('api-auth/', include('rest_framework.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
