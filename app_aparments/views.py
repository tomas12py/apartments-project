from .serializer import ApartmentSerializer,UserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from app_aparments.utils import validate_id
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Apartment

class AparmentMethodsById(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request,id):
        validated_id,error = validate_id(id)
        if error:
            return error
        aparment = get_object_or_404(Apartment,pk = validated_id)
        serializer = ApartmentSerializer(aparment)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,id):
        validated_id,error = validate_id(id)
        if error:
            return error
        aparment = get_object_or_404(Apartment,pk = validated_id)
        serializer = ApartmentSerializer(aparment,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("The aparment was modified",status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        validated_id,error = validate_id(id)
        if error:
            return error
        apartment = get_object_or_404(Apartment,pk = validated_id)
        apartment.delete()
        return Response("The aparment was eliminated",status=status.HTTP_204_NO_CONTENT)

    
    
class AparmentGeneralMethods(APIView):
    def get (self,request):
        apartments = Apartment.objects.all()
        apartments_serializer = ApartmentSerializer(apartments,many = True)
        return Response(apartments_serializer.data)
    
    def post(self,request):
        serializer = ApartmentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("The aparment was created",status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class UserRegister(APIView):

    def post(self,request):
        serializer = UserRegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("User has been created",status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        users  = User.objects.all()
        serializer = UserRegistrationSerializer(users,many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,id):
        validated_id,error = validate_id(id)
        if error:
            return error
        user = get_object_or_404(User,pk = validated_id)
        serializer = UserRegistrationSerializer(user,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("The user was updated",status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        validated_id,error = validate_id(id)
        if error:
            return error
        user = get_object_or_404(User,pk = validated_id)
        user.delete()
        return Response("The user was eliminated",status= status.HTTP_204_NO_CONTENT)