from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Ad
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsPublisherOrReadOnly
from .serializers import AdSerializer
from .paginations import StandardResultPagination

class AdListView(APIView , StandardResultPagination):
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self , request):
        query_set = Ad.objects.filter(is_public=True)
        result = self.paginate_queryset(queryset=query_set , request=request)
        serializer = AdSerializer(instance=result , many=True)
        return self.get_paginated_response(serializer.data)


class AdCreateView(APIView):
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,)
    def post(self, request, *args ,**kwargs):
        serializer = AdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['publisher'] = self.request.user
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class AdDetailEditView(APIView):
    serializer_class = AdSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = [IsAuthenticated, IsPublisherOrReadOnly]

    def get_query(self):
        try:
            instance = Ad.objects.get(id=self.kwargs['pk'])
            self.check_object_permissions(self.request, instance)
            return instance

        except Ad.DoesNotExist :
            return Response({'Message': "There isn't this ad "}, status.HTTP_404_NOT_FOUND)


    def get(self, request, pk):
        instance = self.get_query()
        serializer = AdSerializer(instance=instance)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        instance = self.get_query()
        serializer = AdSerializer(data=request.data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        instance = self.get_query()
        instance.delete()
        return Response(status=status.HTTP_200_OK)










