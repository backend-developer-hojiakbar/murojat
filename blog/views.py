from rest_framework import viewsets
from .models import Passport
from .serializers import PassportSerializer, PetitionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PassportCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PassportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class PetitionCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PetitionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
