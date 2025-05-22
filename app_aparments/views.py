from .serializer import ApartmentSerializer
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