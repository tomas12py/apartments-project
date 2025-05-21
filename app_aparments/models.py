from django.db import models

class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        abstract = True

class Apartment(TimeStamped):
    title = models.CharField(max_length=150,blank=False)
    price = models.IntegerField(blank=False)
    rooms = models.IntegerField(blank=False)
    bathrooms = models.IntegerField(blank=False)
    address = models.CharField(max_length=100,blank=False)
    location = models.CharField(max_length=50,blank=False)
    square_meters = models.FloatField(blank=False)
    images = models.ImageField(blank=False)
    description = models.CharField(max_length=300,blank=False)

    class Meta():
        db_table = "apartment"

