from django.urls import path

from . import views

app_name = "users_app"

urlpatterns = [
    path('register/',views.RegisterUser.as_view(),name='register'),
    path('login/', views.CustomObtainAuthToken.as_view(), name="login"),
    path('logout/',views.Logout.as_view(),name='logout'),
    
]