from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


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
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    followed_tags = models.ManyToManyField(Hashtag)
    # TODO - add upload_to parameter to upload to specific folder
    image = models.ImageField(null=True, blank=True)
    # TODO - change this to address field later
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class Store(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    store_name = models.CharField(max_length=200, unique=True)
    # TODO - change this to address field later
    location = models.TextField()
    description = models.TextField(blank=True)
    # TODO - add upload_to parameter to upload to specific folder
    store_img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.store_name


class Look(models.Model):
    # look gets deleted when store is deleted
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Hashtag)

    likes = models.IntegerField(default=0)
    # TODO - add upload_to parameter to upload to specific folder
    image = models.ImageField(null=True)
    location = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]


class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    look = models.OneToOneField(Look, on_delete=models.DO_NOTHING)

    item_name = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField(blank=True)
    stock = models.IntegerField(default=0)
    # TODO - add upload_to parameter to upload to specific folder
    image = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.item_name
