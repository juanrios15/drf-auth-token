from django.contrib import admin
from django.urls import include, path

from rest_framework.authtoken import views

from users.views import CustomObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', CustomObtainAuthToken.as_view()),
    path('users/', include('users.urls'))
]
