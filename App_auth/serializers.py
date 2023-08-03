from rest_framework.serializers import ModelSerializer
from App_auth.models import CustomUser, UserProfile


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password', 'is_active']
        extra_kwargs = {
            'is_active': {'read_only': True},
            'id': {'read_only': True},
        }

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

        extra_kwargs = {
            'user': {'read_only': True}
        }