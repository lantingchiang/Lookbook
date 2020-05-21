from django.db import models


class Store(models.Model):
    # TODO - figure out smart way to store image
    store_name = models.CharField(max_length=200, unique=True)
    location = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.store_name


class Hashtag(models.Model):
    # TODO - catch error when unique constraint is violated
    tag = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.tag


class Look(models.Model):
    # look gets deleted when store is deleted
    store = models.ForeignKey(Hashtag, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Hashtag)
    likes = models.IntegerField(default=0)
    # TODO - image field


class Product(models.Model):
    item_name = models.CharField(max_length=200, unique=True)
    store = models.ForeignKey(Hashtag, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Hashtag)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    details = models.TextField()
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.item_name
