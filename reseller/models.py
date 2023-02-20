from django.db import models
from common.models import Seller

# Create your models here.

class Product(models.Model):
    seller = models.ForeignKey(Seller,on_delete = models.CASCADE)
    name = models.CharField(max_length= 30)
    number = models.BigIntegerField()
    description = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='product/')



