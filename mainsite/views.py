from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.views.generic import ListView, TemplateView
from django.views import View
#from django.shortcuts import get_object_or_404
from allauth.account.views import SignupView
from rest_framework import viewsets, permissions
#from rest_framework.response import Response

from mainsite.forms import UserSignupForm, SellerSignupForm
from mainsite.serializers import UserSerializer, ProductSerializer, OrdersSerializer, LookSerializer
from mainsite.models import User, Product, Orders, Profile, Look
from mainsite.permissions import IsOwnerOrReadOnly
from mainsite.permissions import IsStaffOrTargetUser

import json
import logging

class HomeView(TemplateView):
    template_name = "home.html"


class LookViewSet(viewsets.ModelViewSet):
    """
    list:
    Return a list of products with partial information for each product.

    retrieve:
    Return a single product with all information fields present.

    update:
    Update all fields in the product.
    You must specify all of the fields or use a patch request.

    partial_update:
    Update certain fields in the product.
    Only specify the fields that you want to change.

    destroy:
    Delete a product. Consider marking the product as inactive instead of deleting the product.
    """

    """
    def get_permissions(self):

        # Instantiates and returns the list of permissions that this view requires.

        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdmin]
        return [permission() for permission in permission_classes]
    """
    queryset = Look.objects.all()
    serializer_class = LookSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )
    def list(self, request):
        """
        Returns list of all products
        """
        # TODO - figure out filtering based on tags
        serializer = LookSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        look = get_object_or_404(self.queryset, pk=pk)
        serializer = LookSerializer(look)
        return Response(serializer.data.get("product", None))

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-name')
    serializer_class = ProductSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all().order_by('-id')
    serializer_class = OrdersSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(owner=user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProfileViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return a single profile with all information fields present.

    update:
    Update all fields in the profile.
    You must specify all of the fields or use a patch request.

    partial_update:
    Update certain fields in the profile.
    Only specify the fields that you want to change.

    destroy:
    Delete a profile. Consider marking the profile as inactive instead of deleting the profile.
    """

    pass


class HashtagView(View):
    def get(self, request):
        """
        Front end will likely need to pass the hashtag name in some request field or in url.
        https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-display/#dynamic-filtering
        """
        return HttpResponse("Renders all looks labeled by this hashtag in chronological order")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return (permissions.AllowAny() if self.request.method == 'POST' else IsStaffOrTargetUser()),

    def perform_create(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)

    def perform_update(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)


class CustomSignupView(TemplateView):
    template_name = "accounts/signup.html"


class UserSignupView(SignupView):
    template_name = "accounts/user_signup.html"
    form_class = UserSignupForm


class SellerSignupView(SignupView):
    template_name = "accounts/seller_signup.html"
    form_class = SellerSignupForm
