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
from mainsite.views import SellerSignupView, BuyerSignupView, SignupView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("mainsite.urls")),
    path("accounts/signup/seller", SellerSignupView.as_view(), name="seller-signup"),
    path("accounts/signup/user", BuyerSignupView.as_view(), name="buyer-signup"),
    path("accounts/signup", SignupView.as_view(), name="signup"),
    path("accounts/", include("allauth.urls")),
    path("", include("frontend.urls")),
    # won't need this after linking frontend to mainsite
    path("core/api/", include("core.api.urls")),
]
