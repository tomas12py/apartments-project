from app_aparments.models import Apartment
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse


class UserTests(APITestCase):

    def setUp(self):
        self.url = reverse('apartment')
        self.user = User.objects.create_user(username = 'alberto',password = '1234')
        self.client.force_authenticate(user = self.user)

    def test_get_all_apartment(self):
        response = self.client.get(self.url,format = 'json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIsInstance(response.data,list)
    
    def test_create_apartment(self):
        data = {
        "title": "Seven apartment",
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
        }
    
        response = self.client.post(self.url,data,format = 'json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertTrue(Apartment.objects.filter(title = 'Seven apartment').exists())