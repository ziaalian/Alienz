from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    
    def __str__(self):
        return self.name



class Store(models.Model):
    name = name = models.CharField(max_length=200)
    address = models.CharField(max_length=50)
    phone = models.IntegerField()
    store_category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    store = models.CharField(max_length=50)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
    store = models.ForeignKey('Store', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
