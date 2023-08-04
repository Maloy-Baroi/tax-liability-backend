import uuid
from django.utils import timezone
from django.db import models
from App_auth.models import CustomUser, UserProfile


class MonthlyTaxPaymentCheck(models.Model):
    tax_payer = models.ForeignKey('TaxPayer', on_delete=models.CASCADE)
    payment_date = models.DateField()
    month_of_payment = models.IntegerField(default=1)
    year_of_payment_month = models.IntegerField(default=2023)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.tax_payer} - {self.payment_date}"
    
    class Meta:
        ordering = ['-payment_date']


class Notification(models.Model):
    tax_payer = models.ForeignKey('TaxPayer', on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    sent_date = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.tax_payer} - {self.message}"
    
    class Meta:
        ordering = ['-sent_date']

def calculate_salary(total_salary):

    if total_salary <= 400000:
        tax_rate = 0.10
        exemption_amount = 2500
    elif total_salary <= 800000:
        tax_rate = 0.15
        exemption_amount = 5000
    else:
        tax_rate = 0.20
        exemption_amount = 10000

    salary_tax = (total_salary * tax_rate) - exemption_amount
    final_salary = total_salary - salary_tax

    return salary_tax



class TaxPayer(models.Model):
    TIN_LENGTH = 12
    TIN_CHOICES = [
        ('individual', 'Individual'),
        ('business', 'Business'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    tax_type = models.CharField(max_length=20, choices=TIN_CHOICES, default='individual')
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)
    nid = models.PositiveIntegerField(unique=True)
    tin = models.PositiveIntegerField(unique=True)
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}: ({self.tin})"

    class Meta:
        verbose_name = "Tax Payer"
        verbose_name_plural = "Tax Payers"

    def save(self, *args, **kwargs):
        # Generate a unique TIN using uuid4() and assign it to the instance before saving
        if not self.pk:
            self.tin = self.generate_unique_tin()
        super().save(*args, **kwargs)

    def generate_unique_tin(self):
        # Generate a unique TIN using uuid4()
        tin = str(uuid.uuid4().int)[:self.TIN_LENGTH]
        while TaxPayer.objects.filter(tin=tin).exists():
            # Regenerate TIN if it already exists in the database
            tin = str(uuid.uuid4().int)[:self.TIN_LENGTH]
        return tin

    def check_monthly_tax_payment(self):
        # Get the current date
        today = timezone.now().date()

        # Check if the taxpayer has made monthly tax payments for this month
        if not self.monthlytaxpaymentcheck_set.filter(payment_date__month=today.month).exists():
            # Send a notification if the taxpayer has not made the payment
            message = f"Monthly tax payment is pending for {today.strftime('%B %Y')}."
            Notification.objects.create(tax_payer=self, message=message)
        else:
            # Delete the notification if the taxpayer has made the payment
            Notification.objects.filter(tax_payer=self).delete()


