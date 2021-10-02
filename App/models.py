from django.db import models



# Create your models here.
class donors(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    phone = models.CharField(max_length=10)
    blood = models.CharField(max_length=5)