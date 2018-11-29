from django.db import models
from decimal import *
from currencies.models import Currency

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=254, default='')
  brand = models.CharField(max_length=50, default='')
  sku = models.CharField(max_length=50, default='')
  description = models.TextField()
  image = models.ImageField(upload_to='images')
  price = models.DecimalField(max_digits=6, decimal_places=2)
  stock = models.IntegerField(default=0)
  
  @property
  def converted_price(self):
    currency = Currency.objects.get(name="USD")
    value = round( self.price * Decimal(currency.rate),2)
    return "{0} {1}".format(currency.symbol, value)
  def __str__(self):
    return self.name


class Category(models.Model):
  name = models.CharField(max_length=254, null=False, blank=False)
  