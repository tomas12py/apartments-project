from app_aparments.api.user.serializer import  UserRegistrationSerializer
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from app_aparments.utils import validate_id
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status

class UserRegister(APIView):

    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User has been created"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        users = User.objects.all()
        serializer = UserRegistrationSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        validated_id, error = validate_id(id)
        if error:
            return error
        user = get_object_or_404(User, pk=validated_id)
        serializer = UserRegistrationSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "The user was updated"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        validated_id, error = validate_id(id)
        if error:
            return error
        user = get_object_or_404(User, pk=validated_id)
        user.delete()
        return Response({"message": "The user was eliminated"}, status=status.HTTP_204_NO_CONTENT)
