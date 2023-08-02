from django.db import models
from django.utils import timezone
from App_tax_payer.models import TaxPayer


class WarningLetter(models.Model):
    warningFor = models.ForeignKey(TaxPayer, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    content = models.TextField()
    issued_date = models.DateField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Warning Letter for {self.warningFor.full_name} - {self.subject}"
