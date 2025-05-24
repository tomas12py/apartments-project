from .serializer import ApartmentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Apartment

class GetAllAparments(APIView):
    def get (self,request):
        apartments = Apartment.objects.all()
        apartments_serializer = ApartmentSerializer(apartments,many = True)
        return Response(apartments_serializer.data)
    
class CreateAparment(APIView):
    def post(self,request):
        serializer = ApartmentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("The aparment was created",status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class GetAparmentById(APIView):
    def get(self,request,id):
        aparment = get_object_or_404(Apartment,pk = id)
        serializer = ApartmentSerializer(aparment)
        return Response(serializer.data)
    
class EditAparmentById(APIView):
    def put(self,request,id):
        aparment = get_object_or_404(Apartment,pk = id)
        serializer = ApartmentSerializer(aparment,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("The aparment was modified",status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class DeleteAparmentById(APIView):
    def delete(self,request,id):
        apartment = get_object_or_404(Apartment,pk = id)
        apartment.delete()
        return Response("The aparment was eliminated",status=status.HTTP_204_NO_CONTENT)