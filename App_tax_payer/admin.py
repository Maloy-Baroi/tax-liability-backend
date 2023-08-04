from django.contrib import admin
from App_tax_payer.models import *

# Register your models here.
admin.site.register(TaxPayer)
admin.site.register(Notification)
admin.site.register(MonthlyTaxPaymentCheck)

