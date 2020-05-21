from django.urls import path
from .views import HomeView, FeedView, ProfileView, HashtagView, ProductView

urlpatterns = [
    path("", HomeView.as_view()),
    path("feed/<username>", FeedView.as_view()),
    path("profile/<username>", ProfileView.as_view()),
    path("/<hashtag>", HashtagView.as_view()),
    path("/<store>/<product>", ProductView.as_view()),
]
