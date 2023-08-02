# Generated by Django 4.2.3 on 2023-08-02 00:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App_tax_payer', '0003_notification_monthlytaxpaymentcheck'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxpayer',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
