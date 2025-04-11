from django.db import models

# Create your models here.
class library(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    edition = models.CharField(max_length=15)
    price = models.FloatField()