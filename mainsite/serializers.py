from rest_framework import serializers
from django.contrib.auth import get_user_model
from mainsite.models import (
    Hashtag,
    User,
    Profile,
    Store,
    Look,
    Product,
    Orders,
    ProductImage,
)

class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'is_seller', 'products')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ["user", "store_name", "location", "phonenumber", "description", "store_img"]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["image", "image_type"]


class ProductSerializer(serializers.ModelSerializer):
    # TODO store = StoreSerializer()
    owner = serializers.ReadOnlyField(source='owner.username')
    #image = serializers.ImageField(source="productimage.images", default=None)

    class Meta:
        model = Product
        #fields = ["id", "store", "name", "price", "details", "stock", "image_url", "created_at", "category", "rating", "owner"]
        fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Orders
        fields = '__all__'

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
