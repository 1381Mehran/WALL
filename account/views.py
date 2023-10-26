from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserAccountSerializer


class UserView(APIView):
    serializer_class = UserAccountSerializer
    permission_classes = [IsAuthenticated]

    def get(self , request):
        user = request.user
        serializer = UserAccountSerializer(instance=user)
        return Response(serializer.data , status=status.HTTP_200_OK)


    def put(self , request):
        user = request.user
        serializer = UserAccountSerializer(data=request.data , instance=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

