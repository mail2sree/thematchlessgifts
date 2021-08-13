from django.db import models
from django.db.models.base import ModelState

# Create your models here.
class Product(models.Model):

    def __str__(self):
        return self.title
    title = models.CharField(max_length=200)
    price = models.FloatField()
    disount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=500)

class Order(models.Model):
    items = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    address2 = models.CharField(max_length=1000)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    orderstatus = models.CharField(max_length=200)
    total = models.CharField(max_length=200)