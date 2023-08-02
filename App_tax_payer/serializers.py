# taxpayer/serializers.py
from rest_framework import serializers
from .models import TaxPayer, MonthlyTaxPaymentCheck


class TaxPayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxPayer
        fields = '__all__'

        extra_kwargs = {
            'tin': {'read_only': True}
        }


class MonthlyTaxPaymentCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyTaxPaymentCheck
        fields = '__all__'
