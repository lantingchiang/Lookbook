from rest_framework import serializers
from django.contrib.auth import get_user_model
from mainsite.models import (
    Hashtag,
    User,
    Profile,
    Store,
    Look,
    Product,
    ProductImage,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "first_name", "last_name", "is_seller"]


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ["user", "store_name", "location", "phonenumber", "description", "store_img"]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["image", "image_type"]


class ProductSerializer(serializers.ModelSerializer):
    store = StoreSerializer()
    image = serializers.ImageField(source="productimage.images", default=None)

    class Meta:
        model = Product
        fields = ["store", "item_name", "price", "details", "stock", "image", "created_at"]


class LookSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(slug_field="tag", queryset=Hashtag.objects.all(), many=True)
    product = ProductSerializer()

    class Meta:
        model = Look
        fields = ["tags", "product", "likes", "image", "created_at"]


class HashtagSerializer(serializers.ModelSerializer):
    look_set = LookSerializer()

    class Meta:
        model = Hashtag
        fields = ["tag", "look_set"]
