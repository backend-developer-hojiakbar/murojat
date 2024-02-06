from rest_framework import serializers
from .models import Passport, Petition

class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passport
        fields = ['id', 'first_name', 'last_name', 'passport_series', 'passport_number', 'phone_number']

class PetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Petition
        fields = ['id', 'government', 'appealType', 'message']