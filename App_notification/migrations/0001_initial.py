# Generated by Django 4.2.4 on 2023-08-04 09:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('App_tax_payer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WarningLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('issued_date', models.DateField(default=django.utils.timezone.now)),
                ('is_read', models.BooleanField(default=False)),
                ('warningFor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_tax_payer.taxpayer')),
            ],
        ),
    ]
