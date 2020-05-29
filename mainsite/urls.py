from django.urls import path
from .views import (
    HomeView,
    FeedView,
    ProfileView,
    HashtagView,
    ProductView,
    LoginView,
    SignupView,
    LogoutView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("feed/<username>/", FeedView.as_view(), name="feed"),
    path("profile/<username>/", ProfileView.as_view(), name="profile"),
    path("<hashtag>/", HashtagView.as_view(), name="hashtag"),
    path("<store>/<product>/", ProductView.as_view(), name="product"),
    path("accounts/login", LoginView.as_view(), name="login"),
    path("accounts/signup", LoginView.as_view(), name="signup"),
    path("accounts/logout", LogoutView.as_view(), name="logout"),
]
