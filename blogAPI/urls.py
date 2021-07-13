from django.urls import path

from . import views

app_name = "posts_app"

urlpatterns = [
    path('userposts/',views.UserPostsView.as_view(),name='userposts'),
]