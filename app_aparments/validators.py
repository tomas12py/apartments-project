from rest_framework import serializers

def number_greater_than_zero(value):
    if value == 0:
        raise serializers.ValidationError("The number must be greater than zero")