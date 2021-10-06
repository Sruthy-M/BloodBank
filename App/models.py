from django.db import models

# Create your models here.

class Userinfo(models.Model):

    name                    = models.CharField(max_length=100)
    age                     = models.IntegerField()
    blood_group             = models.CharField(max_length=10)
    phone_number            = models.IntegerField()
    unit                    = models.CharField(max_length=50)
    date_of_donation        = models.DateField()


