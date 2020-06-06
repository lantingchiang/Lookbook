from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class Hashtag(models.Model):
    tag = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.tag


class User(AbstractUser):
    # inherit username, password, email, first_name, and last_name fields
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
    store_name = models.CharField(max_length=200, unique=True)
    # TODO - change this to address field later
    location = models.TextField()
    phonenumber = PhoneNumberField(default="")
    description = models.TextField(blank=True, default="")
    # TODO - add upload_to parameter to upload to specific folder
    store_img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.store_name


class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    item_name = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField(blank=True)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.item_name


class Look(models.Model):
    tags = models.ManyToManyField(Hashtag)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    likes = models.IntegerField(default=0)
    # TODO - add upload_to parameter to upload to specific folder
    image = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]


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
