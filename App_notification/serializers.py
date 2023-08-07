# serializers.py
from rest_framework import serializers

from App_notification.models import WarningLetter
from App_tax_payer.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class WarningLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarningLetter
        fields = '__all__'
