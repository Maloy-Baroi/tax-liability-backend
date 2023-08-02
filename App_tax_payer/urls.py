# taxpayer/urls.py
from django.urls import path
from .views import TaxPayerListCreateView, TaxPayerRetrieveUpdateView, MonthlyTaxPaymentCheckListCreateView, \
    MonthlyTaxPaymentCheckRetrieveUpdateView

urlpatterns = [
    path('', TaxPayerListCreateView.as_view(), name='taxpayer-list-create'),
    path('taxpayers/<int:pk>/', TaxPayerRetrieveUpdateView.as_view(), name='taxpayer-retrieve-update'),
    path('monthly-tax-payments/', MonthlyTaxPaymentCheckListCreateView.as_view(),
         name='monthly-tax-payment-list-create'),
    path('monthly-tax-payments/<int:pk>/', MonthlyTaxPaymentCheckRetrieveUpdateView.as_view(),
         name='monthly-tax-payment-retrieve-update'),
]
