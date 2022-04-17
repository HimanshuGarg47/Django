from django.urls import path , include
from . import views
urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank-page" ,views.ThankView.as_view()),
    path("reviews", views.ReviewListView.as_view()),
    path("reviews/favorite", views.AddFavoriteView.as_view()),
    path("reviews/<int:pk>", views.SingleReviewView.as_view(), name="dreview"),
]
