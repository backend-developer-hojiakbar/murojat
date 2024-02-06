import random

from django.db import models

# Create your models here.
class Passport(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    passport_series = models.CharField(max_length=10)
    passport_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)

    def create_verify_code(self):
        code = "".join([str(random.randint(0, 10000) % 10) for _ in range(4)])
        print("Cod telefon uchun -->", code)
        return code

    def __str__(self):
        return self.first_name
class Government(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
class AppealType(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
class Petition(models.Model):
    government = models.ForeignKey(Government, on_delete=models.CASCADE)
    appealType = models.ForeignKey(AppealType, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.message
