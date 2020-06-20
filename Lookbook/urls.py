"""Lookbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mainsite.views import ProductViewSet, OrdersViewSet, UserViewSet, SellerSignupView, UserSignupView, CustomSignupView

from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
#from cart.views import ProductsViewSet, OrdersViewSet, UserViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrdersViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("home/", include("mainsite.urls")),
    path("accounts/signup/seller/", SellerSignupView.as_view(), name="seller_signup"),
    path("accounts/signup/user/", UserSignupView.as_view(), name="user_signup"),
    path("accounts/signup/", CustomSignupView.as_view(), name="signup"),
    path("accounts/", include("allauth.urls")),
    path("api-auth/", include('rest_framework.urls', namespace='rest_framework')),
    path("api-token-auth/", obtain_jwt_token),
    path("api-token-verify/", verify_jwt_token),
    path("api-token-refresh/", refresh_jwt_token)
    # path("", include("frontend.urls")),
]