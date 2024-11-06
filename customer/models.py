from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=11)
    balance = models.IntegerField()
    picture = models.ImageField(default="fallback.jpg")