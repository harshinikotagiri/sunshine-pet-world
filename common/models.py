from django.db import models

# Create your models here.
class contactform(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    text = models.CharField(max_length=100)

class adminprofile(models.Model):
    name = models.CharField(max_length=20)
    number = models.CharField(max_length=12)
    officeaddress = models.CharField(max_length=80)
    email = models.EmailField()

class registration(models.Model):
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=20) 
    contact = models.CharField(max_length=12)
    type = models.CharField(max_length=15)
    email = models.EmailField()

class adminaddhht(models.Model):
    username = models.CharField(max_length=30)
    fullname = models.CharField(max_length=20)
    type = models.CharField(max_length=15)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    experience = models.CharField(max_length=15)
    description = models.CharField(max_length=500)
    chooseanimage = models.ImageField()