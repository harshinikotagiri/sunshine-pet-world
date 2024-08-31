from django.db import models

# Create your models here.
class handlerprofile(models.Model):
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=10)
    phonenumber = models.CharField(max_length=12)
    email = models.EmailField()
    experience = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
