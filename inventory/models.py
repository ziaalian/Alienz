from unittest.util import _MAX_LENGTH
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    store = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.IntegerField()

    def __str__(self):
        return self.name
