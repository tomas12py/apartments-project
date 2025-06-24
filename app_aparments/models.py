from .validators import number_greater_than_zero
from django.db import models


class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        abstract = True


class Apartment(TimeStamped):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, blank=False)
    price = models.IntegerField(blank=False, validators=[
                                number_greater_than_zero])
    rooms = models.IntegerField(blank=False)
    bathrooms = models.IntegerField(blank=False)
    address = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=50, blank=False)
    square_meters = models.FloatField(blank=False)
    images = models.URLField(max_length=350, blank=False)
    description = models.CharField(max_length=300, blank=False)
    garage = models.IntegerField(blank=True,default=0)
    elevator = models.BooleanField(blank=True)
    pool = models.BooleanField(blank=True)



    class Meta():
        db_table = "apartment"

    def __str__(self):
        return f" Aparment {id}"
