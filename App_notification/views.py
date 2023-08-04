from django.shortcuts import render
from rest_framework import generics
from App_tax_payer.models import Notification, TaxPayer, MonthlyTaxPaymentCheck
from App_tax_payer.serializers import MonthlyTaxPaymentCheckSerializer
from .serializers import NotificationSerializer, WarningLetterSerializer
from .models import WarningLetter
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist 
from datetime import datetime
from django.db.models import Q


# Create your views here.
class NotificationListView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class UserHomeData(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            user = request.user
            tax_payer = TaxPayer.objects.get(user=user.id)
            current_date = datetime.now().date()
            check_payment = MonthlyTaxPaymentCheck.objects.filter(Q(tax_payer=tax_payer), Q(payment_date__month=current_date.month) & Q(payment_date__year=current_date.year)).first()
            is_paid = check_payment is not None
            check_payments = MonthlyTaxPaymentCheck.objects.filter(Q(tax_payer=tax_payer))
            print(check_payments)
            check_payments_count = check_payments.count()
            if check_payments_count > 3:
                check_payments = check_payments[:3]
            serializer = MonthlyTaxPaymentCheckSerializer(check_payments, many=True)
            return Response({
                             'tax_id': tax_payer.tin,
                             'category': tax_payer.tax_type,
                             'is_paid': is_paid,
                             'transactions': serializer.data
                             })
        except ObjectDoesNotExist:
            return Response({
                             'tax_id': "N/A",
                             'category': "N/A",
                             'is_paid': False,
                             'transactions': []
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