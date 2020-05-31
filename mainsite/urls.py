from django.urls import path
from django.contrib.auth import views as auth_views
from mainsite.views import (
    HomeView,
    FeedView,
    ProfileView,
    HashtagView,
    ProductView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("feed/", FeedView.as_view(), name="feed"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("<hashtag>/", HashtagView.as_view(), name="hashtag"),
    path("<store>/<product>/", ProductView.as_view(), name="product"),
]
