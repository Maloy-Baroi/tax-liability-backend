from django.shortcuts import render
from rest_framework import generics

from App_notification.models import WarningLetter
from App_notification.serializers import WarningLetterSerializer


# Create your views here.
class WarningLetterListCreateView(generics.ListCreateAPIView):
    queryset = WarningLetter.objects.all()
    serializer_class = WarningLetterSerializer


class WarningLetterRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WarningLetter.objects.all()
    serializer_class = WarningLetterSerializer
