from app_aparments.api.aparment.serializer import ApartmentFilteringSerializer, ApartmentImageSerializer
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from app_aparments.api.aparment.serializer import ApartmentSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from drf_spectacular.utils import extend_schema, OpenApiExample
from django_filters.rest_framework import DjangoFilterBackend
from app_aparments.models import Apartment, ApartmentImage
from app_aparments.pagination import CustomPagination
from rest_framework.decorators import throttle_classes
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from app_aparments.api.user import serializer
from rest_framework.response import Response        
from app_aparments.utils import validate_id
from rest_framework.views import APIView
from .filters import ApartmentFiltering
from rest_framework import viewsets
from rest_framework import status

class ApartmentMethodsById(APIView):

    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get(self, request, id):
        validated_id, error = validate_id(id)
        if error:
            return error
        aparment = get_object_or_404(Apartment, pk=validated_id)
        serializer = ApartmentSerializer(aparment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        validated_id, error = validate_id(id)
        if error:
            return error
        aparment = get_object_or_404(Apartment, pk=validated_id)
        serializer = ApartmentSerializer(aparment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "The aparment was modified"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        validated_id, error = validate_id(id)
        if error:
            return error
        apartment = get_object_or_404(Apartment, pk=validated_id)
        apartment.delete()
        return Response({"message": "The aparment was eliminated"}, status=status.HTTP_204_NO_CONTENT)


class ApartmentViewsetFilter(viewsets.ReadOnlyModelViewSet):

   queryset = Apartment.objects.all()
   serializer_class = ApartmentSerializer
   filter_backends = [DjangoFilterBackend]  
   filterset_class = ApartmentFiltering


class ApartmentPagination(APIView, CustomPagination):

    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    @method_decorator(cache_page(60 * 5))
    def get(self, request):
        queryset = Apartment.objects.all()
        page = self.paginate_queryset(queryset, request, view=self)

        if page is not None:
            serializer = ApartmentSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = ApartmentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ApartmentGeneralMethods(APIView):

    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    @extend_schema(
        summary="Get all aparments",
        description="Get each aparment",
        responses={200: ApartmentSerializer, 400: "ErrorSerializer"},
        examples=[
            OpenApiExample(
                "All aparments",
                summary="Response for get each aparment",
                description="This example shows how to get all aparments",
                value={
                    "id": 13,
                    "created_at": "2025-05-28T03:55:15.493777Z",
                    "updated_at": "2025-05-28T03:55:15.494313Z",
                    "title": "Seven aparment",
                    "price": 100,
                    "rooms": 2,
                    "bathrooms": 0,
                    "address": "hola",
                    "location": "0",
                    "square_meters": 50.75,
                    "images": "https://www.notion",
                    "description": "Aparment for sell"
                }
            ),
            OpenApiExample(
                "Error example",
                summary="Error for get all aparments",
                value={
                    "error": "There was a error"
                },
                status_codes=['400']
            )
        ],
        tags=["Aparment"]
    )
    def get(self, request):
        apartments = Apartment.objects.all()
        apartments_serializer = ApartmentSerializer(apartments, many=True)
        return Response(apartments_serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Create an aparment",
        description="With this endpoint you can create an aparment",
        responses={201: ApartmentSerializer, 400: "Bad request"},
        examples=[OpenApiExample(
            "Create an aparment",
            summary="Structure for create an aparment",
            description="This example show how to create an aparment",
            value={
                    "id": 13,
                    "created_at": "2025-05-28T03:55:15.493777Z",
                    "updated_at": "2025-05-28T03:55:15.494313Z",
                    "title": "Seven aparment",
                    "price": 100,
                    "rooms": 2,
                    "bathrooms": 0,
                    "address": "hola",
                    "location": "0",
                    "square_meters": 50.75,
                    "images": "https://www.notion",
                    "description": "Aparment for sell"
            }
        ),
            OpenApiExample(
            "Error example",    
            summary="Error for create an aparment",
            value={"error": "There was a error"},
            status_codes=[400]
        )],
        tags=["Aparment"]
    )
    def post(self, request):
        serializer = ApartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "The aparment was created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateImage(APIView):

    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def post(self, request):
        serializer = ApartmentImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "The image was created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
