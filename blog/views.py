from rest_framework import viewsets
from .models import Passport, Petition
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

class NumberOfPeople(APIView):
    def get(self, request, *args, **kwargs):
        names = Passport.objects.all()
        number = names.count()
        print("Odamlar soni -->", number)
        return Response(number, status=status.HTTP_200_OK)
class NumberOfPeopleMonth(APIView):
    def get(self, request, son):
        names = Passport.objects.filter(created_time__month=son)
        number = names.count()
        print("Odamlar soni -->", number)
        return Response(number, status=status.HTTP_200_OK)
class NumberOfConsideredPeople(APIView):
    def get(self, request, *args, **kwargs):
        messages = Petition.objects.all()
        number = messages.count()
        print("Xabarlar soni -->", number)
        return Response(number, status=status.HTTP_200_OK)
class NumberOfConsideredPeopleMonth(APIView):
    def get(self, request, son):
        messages = Petition.objects.filter(created_time__month=son)
        number = messages.count()
        print("Odamlar soni -->", number)
        return Response(number, status=status.HTTP_200_OK)