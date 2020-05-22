from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class Store(models.Model):
    store_name = models.CharField(max_length=200, unique=True)
    location = models.TextField()
    description = models.TextField()
    store_img = models.ImageField(upload_to=store_name, null=True)

    def __str__(self):
        return self.store_name


class Hashtag(models.Model):
    tag = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.tag


class Look(models.Model):
    # look gets deleted when store is deleted
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Hashtag)

    likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to=store.store_name, null=True)
    location = models.TextField()


class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    look = models.OneToOneField(Look)

    item_name = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to=store.store_name, null=True)

    def __str__(self):
        return self.item_name
