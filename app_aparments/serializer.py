from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Apartment

class ApartmentSerializer(serializers.ModelSerializer):

    class Meta():
        model = Apartment
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields  = ('username','password')

    def create(self,validated_data):
        user  = User(
            username = validated_data["username"],
            password = validated_data["password"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user