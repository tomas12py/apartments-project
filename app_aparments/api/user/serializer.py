from django.contrib.auth.models import User
from rest_framework import serializers  


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ('username', 'password','id')

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            password=validated_data["password"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        if ("password" in validated_data):
            instance.set_password(validated_data["password"])
        instance.save()
        return instance
