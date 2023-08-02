# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from App_tax_payer.models import Notification
from .models import WarningLetter


@receiver(post_save, sender=Notification)
def generate_warning_letter(sender, instance, created, **kwargs):
    if created:  # Only act on new notifications, not updates to existing ones
        tax_payer = instance.tax_payer
        notifications_count = tax_payer.notification_set.count()

        # Check if the TaxPayer has more than 3 notifications
        if notifications_count > 3:
            # Create a warning letter for the TaxPayer
            subject = "Warning: Too Many Notifications"
            content = f"Dear {tax_payer.full_name}, you have received {notifications_count} notifications, which exceeds the limit of 3. Please take necessary actions. Regards, Tax Department."
            WarningLetter.objects.create(warningFor=tax_payer, subject=subject, content=content)
