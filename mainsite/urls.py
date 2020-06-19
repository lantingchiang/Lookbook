from django.urls import path
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from mainsite.views import (
    HomeView,
    ProfileViewSet,
    HashtagView,
    ProductViewSet,
)

# router = DefaultRouter()
# router.register(r"products", ProductViewSet, basename="products")

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    # path("profile/", ProfileViewSet.as_view(), name="profile"),
    # path("<hashtag>/", HashtagView.as_view(), name="hashtag"),
]

# urlpatterns += router.urls
