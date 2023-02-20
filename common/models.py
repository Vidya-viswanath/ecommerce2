from django.db import models

#
#  Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=25)
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=30)
   
class Seller(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=25)
    photo = models.ImageField(upload_to='seller/')
    comp_name = models.CharField(max_length=50)
    acc_name = models.CharField(max_length=70)
    ifsc = models.CharField(max_length=30)
    branch = models.CharField(max_length=75)
    acc_number = models.CharField(max_length=50)
    username = models.CharField(max_length=50,default="")
    password = models.CharField(max_length=20,default="")




