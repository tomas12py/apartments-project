from django.contrib.auth.models import User
from .validators import is_letter_and_spaces
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
    
    def update(self,instance,validated_data):
        instance.username = validated_data.get("username",instance.username)
        if ("password" in validated_data):
            instance.set_password(validated_data["password"])
        instance.save()
        return instance
    
class AparmentFilteringSerializer(serializers.Serializer):
    location  = serializers.CharField(required = False,max_length = 150,validators = [is_letter_and_spaces])