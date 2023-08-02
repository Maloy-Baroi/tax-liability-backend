from django.shortcuts import render
from rest_framework import generics
from App_tax_payer.models import Notification
from .serializers import NotificationSerializer, WarningLetterSerializer
from .models import WarningLetter


# Create your views here.
class NotificationListView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class WarningLetterListCreateView(generics.ListCreateAPIView):
    queryset = WarningLetter.objects.all()
    serializer_class = WarningLetterSerializer


class WarningLetterRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WarningLetter.objects.all()
    serializer_class = WarningLetterSerializer
