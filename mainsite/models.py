from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.postgres.fields import ArrayField
from decimal import Decimal


class Hashtag(models.Model):
    tag = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.tag


class User(AbstractUser):
    # inherit username, password, email, first_name, and last_name fields
    email = models.EmailField(unique=True, blank=False)
    is_seller = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Profile(models.Model):
    GENDER_CHOICES = [("F", "Female"), ("M", "Male"), ("O", "Other")]

    AGE_CHOICES = [
        ("A", "18-"),
        ("B", "18-25"),
        ("C", "25-35"),
        ("D", "35-45"),
        ("E", "45+"),
    ]

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    followed_tags = models.ManyToManyField(Hashtag)
    # TODO - add upload_to parameter to upload to specific folder
    image = models.ImageField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, default="")
    age = models.CharField(max_length=1, choices=AGE_CHOICES, blank=True, default="")
    # TODO - change this to address field later
    address = models.TextField(blank=True)
    phonenumber = PhoneNumberField(default="")

    def __str__(self):
        return self.user.username


class Store(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    store_name = models.CharField(max_length=200, unique=True, default="")
    # TODO - change this to address field later
    location = models.TextField(default="")
    phonenumber = PhoneNumberField(default="")
    description = models.TextField(blank=True, default="")
    # TODO - add upload_to parameter to upload to specific folder
    store_img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.store_name


class Product(models.Model):
    # TODO store = models.ForeignKey(Store, on_delete=models.CASCADE, default="")
    name = models.CharField(max_length=200, unique=True, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))
    details = models.TextField(default="Product description.")
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    category = models.CharField(max_length=30, default="")
    rating = models.PositiveSmallIntegerField(default=0)
    image_url = models.TextField(default="")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="products", null=True, on_delete=models.CASCADE
    )

    class Meta:
        # ordering = ["-created_at"]
        db_table = "products"

    def __str__(self):
        return self.name


class Orders(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    products = ArrayField(models.CharField(max_length=50), default=list)
    quantities = ArrayField(models.PositiveIntegerField(), default=list)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))
    delivery_method = models.CharField(max_length=30, default="")
    payment_method = models.CharField(max_length=30, default="")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="orders", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "orders"


class Look(models.Model):
    tags = models.ManyToManyField(Hashtag)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    likes = models.IntegerField(default=0)
    # TODO - add upload_to parameter to upload to specific folder
    image = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.product.item_name


class ProductImage(models.Model):
    IMAGE_CLASSIFICATION = [
        ("F", "Front"),
        ("B", "Back"),
        ("S", "Side"),
        ("O", "Other"),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # TODO - add upload_to parameter to upload to specific folder
    image = models.ImageField(null=True)
    image_type = models.CharField(max_length=1, choices=IMAGE_CLASSIFICATION)
