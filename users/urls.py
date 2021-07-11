from django.urls import path

from . import views

app_name = "users_app"

urlpatterns = [
    path('logout/',views.Logout.as_view(),name='logout'),
    
]