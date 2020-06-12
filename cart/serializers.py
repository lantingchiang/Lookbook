#from django.contrib.auth.models import User

from rest_framework import serializers
from cart.models import User, Products, Orders
from django.contrib.auth import get_user_model

class ProductsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Products
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Orders
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        #model = User
        #fields = ('id', 'username', 'email', 'password', 'products')
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'is_seller', 'products')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
