from app_aparments.models import Apartment,ApartmentImage
from app_aparments.validators import is_letter_and_spaces
from rest_framework import serializers


class ApartmentImageSerializer(serializers.ModelSerializer):

    class Meta():
        model = ApartmentImage
        fields = '__all__'

class ApartmentSerializer(serializers.ModelSerializer):
    images = ApartmentImageSerializer(many = True,read_only = True)
    class Meta():
        model = Apartment
        fields = '__all__'


class ApartmentFilteringSerializer(serializers.Serializer):
    location = serializers.CharField(
        required=False, max_length=150, validators=[is_letter_and_spaces])
