from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TaxPayer


@receiver(post_save, sender=TaxPayer)
def check_monthly_tax_payment(sender, instance, **kwargs):
    instance.check_monthly_tax_payment()
