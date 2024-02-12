from django.urls import path
from .views import PassportCreateAPIView, PetitionCreateAPIView, NumberOfPeople,\
    NumberOfConsideredPeople, NumberOfPeopleMonth, NumberOfConsideredPeopleMonth


urlpatterns = [
    path('passport/', PassportCreateAPIView.as_view(),name='passportCreate'),
    path('petition/', PetitionCreateAPIView.as_view(), name='petitionCreate'),
    path('number/', NumberOfPeople.as_view(), name='numberOfPeople'),
    path('number/<int:son>/', NumberOfPeopleMonth.as_view(), name='numberOfPeopleMonth'),
    path('considered/', NumberOfConsideredPeople.as_view(), name='numberOfConsidered'),
    path('considered/<int:son>/', NumberOfConsideredPeopleMonth.as_view(), name='numberOfConsideredMonth'),
]