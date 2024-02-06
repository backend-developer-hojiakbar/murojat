from django.urls import path
from .views import PassportCreateAPIView, PetitionCreateAPIView


urlpatterns = [
    path('passport/', PassportCreateAPIView.as_view(),name='passportCreate'),
    path('petition/', PetitionCreateAPIView.as_view(), name='petitionCreate'),
]