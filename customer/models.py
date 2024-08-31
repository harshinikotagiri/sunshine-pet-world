from django.db import models

# Create your models here.
class customeraddpet(models.Model):
    username = models.CharField(max_length=20)
    petname = models.CharField(max_length=20)
    pettype = models.CharField(max_length=10)
    petbreed = models.CharField(max_length=30)
    petcolor = models.CharField(max_length=20)
    petage = models.CharField(max_length=15)
    petgender = models.CharField(max_length=10)
    chooseanimage = models.EmailField()

class customerbooking(models.Model):
    bookingid = models.CharField(max_length=20)
    customerusername = models.CharField(max_length=30)
    hhtusername = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

class customerticket(models.Model):
    username = models.CharField(max_length=20)
    hhtname = models.CharField(max_length=20)
    type = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)
    reason = models.CharField(max_length=500)
    reply = models.CharField(max_length=500)

class customerfeedback(models.Model):
    username = models.CharField(max_length=30)
    hhtname = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
