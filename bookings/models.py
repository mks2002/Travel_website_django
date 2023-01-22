from django.db import models


# Create your models here.


class Booking(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    contact_no = models.CharField(max_length=13)
    no_people = models.IntegerField()
