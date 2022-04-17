from django.urls import path
from . import views



urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("all", views.UserProfileView.as_view())
] 