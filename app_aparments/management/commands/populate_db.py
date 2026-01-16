from django.core.management.base import BaseCommand,CommandError
from app_aparments.models import Apartment
from django.db.utils import IntegrityError


apartment_data = [
   
     {
    "title": "apartment of someone",
    "price": 100,
    "rooms": 2,
    "bathrooms": 0,
    "address": "hola",
    "location": "0",
    "square_meters": 50.75,
    "description": "Aparment for sell",
    "garage": 0,
    "elevator": False,
    "pool": False,
    "state": "rent"
  },
   {
    "title": "apartment of someone",
    "price": 100,
    "rooms": 2,
    "bathrooms": 0,
    "address": "hola",
    "location": "0",
    "square_meters": 50.75,
    "description": "Aparment for sell",
    "garage": 0,
    "elevator": False,
    "pool": False,
    "state": "rent"
  },
   {
    "title": "apartment of someone",
    "price": 100,
    "rooms": 2,
    "bathrooms": 0,
    "address": "hola",
    "location": "0",
    "square_meters": 50.75,
    "description": "Aparment for sell",
    "garage": 0,
    "elevator": False,
    "pool": False,
    "state": "rent"
  },
   {
    "title": "apartment of someone",
    "price": 100,
    "rooms": 2,
    "bathrooms": 0,
    "address": "hola",
    "location": "0",
    "square_meters": 50.75,
    "description": "Aparment for sell",
    "garage": 0,
    "elevator": False,
    "pool": False,
    "state": "rent"
  },
   {
    "title": "apartment of someone",
    "price": 100,
    "rooms": 2,
    "bathrooms": 0,
    "address": "hola",
    "location": "0",
    "square_meters": 50.75,
    "description": "Aparment for sell",
    "garage": 0,
    "elevator": False,
    "pool": False,
    "state": "rent"
  },

]


class Command(BaseCommand):

    def handle(self,*args,**kwars):

        try:
            for data in apartment_data:
                apartment = Apartment.objects.create(
                    title = data["title"],
                    price = data["price"],
                    rooms = data["rooms"],
                    bathrooms = data["bathrooms"],
                    address = data["address"],
                    location = data["location"],
                    square_meters = data["square_meters"],
                    description = data["description"],
                    garage = data["garage"],
                    elevator = data["elevator"],
                    pool = data["pool"],
                    state = data["state"]
                )

                apartment.full_clean()
                apartment.save()


                self.stdout.write(self.style.SUCCESS(f"The apartment with the id {apartment.id} and name {apartment.title} has been created"))

        except IntegrityError as e:
          raise CommandError((f"There was an error: {e}"))