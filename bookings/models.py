from django.db import models


# Create your models here.


class Bookinghotel(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    contact_no = models.CharField(max_length=13)
    no_people = models.IntegerField()
    username = models.CharField(max_length=30)
    userpassword = models.CharField(max_length=30)
    start = models.DateField(default=None)
    end = models.DateField(default=None)
    hotelname = models.CharField(max_length=80, default=None)
    city = models.CharField(max_length=60, default=None)
    state = models.CharField(max_length=60, default=None)
    current_cost = models.FloatField(default=0.0)
