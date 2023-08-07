# taxpayer/views.py
from rest_framework import generics
from .models import TaxPayer, MonthlyTaxPaymentCheck
from .serializers import TaxPayerSerializer, MonthlyTaxPaymentCheckSerializer
from rest_framework.permissions import IsAuthenticated


class TaxPayerListCreateView(generics.ListCreateAPIView):
    queryset = TaxPayer.objects.all()
    serializer_class = TaxPayerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaxPayerRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = TaxPayer.objects.all()
    serializer_class = TaxPayerSerializer


class MonthlyTaxPaymentCheckListCreateView(generics.ListCreateAPIView):
    queryset = MonthlyTaxPaymentCheck.objects.all()
    serializer_class = MonthlyTaxPaymentCheckSerializer


class MonthlyTaxPaymentCheckRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = MonthlyTaxPaymentCheck.objects.all()
    serializer_class = MonthlyTaxPaymentCheckSerializer
