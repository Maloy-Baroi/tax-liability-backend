from django.shortcuts import render
from rest_framework import generics
from App_tax_payer.models import Notification, TaxPayer
from .serializers import NotificationSerializer, WarningLetterSerializer
from .models import WarningLetter
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist 


# Create your views here.
class NotificationListView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class UserHomeData(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            user = request.user
            print(user.id)
            tax_payer = TaxPayer.objects.get(user=user.id)
            
            return Response({
                             'tax_id': tax_payer.tin,
                             'category': tax_payer.tax_type
                             })
        except ObjectDoesNotExist:
            return Response({
                             'tax_id': "N/A",
                             'category': "N/A"
                             })
        except Exception as e:
            return Response({'error': str(e)}, status=500)


class NotificationCountData(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            user = request.user
            print(user.id)
            tax_payer = TaxPayer.objects.get(user=user.id)
            notifications = Notification.objects.filter(tax_payer=tax_payer).count()
            return Response({'notifications': notifications})
        except ObjectDoesNotExist:
            return Response({'notifications': 0})
        except Exception as e:
            return Response({'error': str(e)}, status=500)
        

class NotificationData(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            user = request.user
            tax_payer = TaxPayer.objects.get(user=user)
            notification_list = Notification.objects.filter(tax_payer=tax_payer)
            serializer = NotificationSerializer(notification_list, many=True)
            return Response({'notification_list': serializer.data})
        except TaxPayer.DoesNotExist:
            return Response({'notification_list': []})