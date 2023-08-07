from rest_framework import generics

from App_tax_payer.models import TaxPayer
from .jwt_checker.decoder import get_user_id_from_jwt
from .models import CustomUser, UserProfile
from .serializers import CustomUserSerializer, UserProfileSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class CustomUserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            user_id = get_user_id_from_jwt(response.data['access'])
            try:
                tax_payer = TaxPayer.objects.get(user=user_id)
                is_tax_payer = True
            except TaxPayer.DoesNotExist:
                is_tax_payer = False
                
            try:
                profile = UserProfile.objects.get(user=user_id)
                exist_profile = True
            except UserProfile.DoesNotExist:
                exist_profile = False
            
            data = response.data
            data['is_tax_payer'] = is_tax_payer
            data['user_id'] = user_id
            data['exist_profile'] = exist_profile
            return Response(data)

        return response

class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserProfileUpdateView(generics.UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]