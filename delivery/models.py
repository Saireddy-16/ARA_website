from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    address=models.CharField(max_length=50)

class Dress(models.Model):
    name = models.CharField(max_length=20)
    photo = models.URLField(max_length=200)
    rating = models.FloatField()
    details = models.CharField(max_length=300)