from rest_framework import serializers
from django.contrib.auth import get_user_model
from mainsite.models import (
    Hashtag,
    User,
    Profile,
    Store,
    Look,
    Product,
)


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ["id", "tag"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email", "first_name", "last_name", "is_seller"]
