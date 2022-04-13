from django.urls import path , include
from . import views
urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank-page" ,views.thanks)
]
