from django.core.validators import MinValueValidator,MaxValueValidator
from app_aparments.api.constants import STATUS_CHOICES
from django.db import models


class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        abstract = True


class Apartment(TimeStamped):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, blank=False)
    price = models.IntegerField(blank=False,validators=[    
                                MinValueValidator(100),MaxValueValidator(100000)])
    rooms = models.IntegerField(blank=False)
    bathrooms = models.IntegerField(blank=False)
    address = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=50, blank=False)
    square_meters = models.FloatField(blank=False)
    description = models.CharField(max_length=300, blank=False)
    garage = models.IntegerField(blank=True,default=0)
    elevator = models.BooleanField(blank=True)
    pool = models.BooleanField(blank=True)
    state = models.CharField(max_length = 10,choices = STATUS_CHOICES, default = 'rent' )

    class Meta():
        db_table = "apartment"

    
    def save(self,*args, **kwargs):
        
        if self.title:
             self.title = self.title.capitalize()   
        super().save(*args, **kwargs)

    def __str__(self):
        return f" Aparment {id}"
    
class ApartmentImage(TimeStamped):
        apartment = models.ForeignKey(Apartment,related_name = 'images',on_delete = models.CASCADE)
        image = models.URLField(max_length = 300)  

        class Meta():
             db_table = "apartment_image"   