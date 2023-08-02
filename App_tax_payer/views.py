# taxpayer/views.py
from rest_framework import generics
from .models import TaxPayer, MonthlyTaxPaymentCheck
from .serializers import TaxPayerSerializer, MonthlyTaxPaymentCheckSerializer


class TaxPayerListCreateView(generics.ListCreateAPIView):
    queryset = TaxPayer.objects.all()
    serializer_class = TaxPayerSerializer


class TaxPayerRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = TaxPayer.objects.all()
    serializer_class = TaxPayerSerializer


class MonthlyTaxPaymentCheckListCreateView(generics.ListCreateAPIView):
    queryset = MonthlyTaxPaymentCheck.objects.all()
    serializer_class = MonthlyTaxPaymentCheckSerializer


class MonthlyTaxPaymentCheckRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = MonthlyTaxPaymentCheck.objects.all()
    serializer_class = MonthlyTaxPaymentCheckSerializer
