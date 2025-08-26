from app_aparments.models import Apartment,AparmentImage
from app_aparments.validators import is_letter_and_spaces
from rest_framework import serializers


class AparmentImageSerializer(serializers.ModelSerializer):

    class Meta():
        model = AparmentImage
        fields = '__all__'

class ApartmentSerializer(serializers.ModelSerializer):
    images = AparmentImageSerializer(many = True,read_only = True)
    class Meta():
        model = Apartment
        fields = '__all__'


class AparmentFilteringSerializer(serializers.Serializer):
    location = serializers.CharField(
        required=False, max_length=150, validators=[is_letter_and_spaces])
