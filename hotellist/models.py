from django.db import models

# Create your models here.

class Hotellist(models.Model):
    name=models.CharField(max_length=80)
    city=models.CharField(max_length=40)
    state=models.CharField(max_length=60)
    star=models.IntegerField(default=0)
    image= models.FileField(
        upload_to="image_folder/", max_length=2500, null=True, default=None)
    current_cost=models.FloatField()
    delete_cost=models.FloatField()